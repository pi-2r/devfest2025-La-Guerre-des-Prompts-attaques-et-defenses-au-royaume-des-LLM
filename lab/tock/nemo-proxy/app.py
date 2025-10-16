"""
Main FastAPI application refactored with modular architecture
"""
import logging
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import html
from fastapi.middleware.cors import CORSMiddleware

# Logging configuration
from config.settings import LOG_LEVEL, CORS_ORIGINS, CORS_METHODS, CORS_HEADERS
logging.basicConfig(level=getattr(logging, LOG_LEVEL))
logger = logging.getLogger(__name__)

# Module imports
from security.sanitizer import sanitize_input
from security.jailbreak_detector import detect_jailbreak_attempt, is_response_blocked
from services import GuardrailsService, BotApiService
from utils.responses import create_error_response, create_success_response, create_fallback_response
from nemoguardrails import RailsConfig, LLMRails

# Service initialization
guardrails_service = GuardrailsService()
bot_service = BotApiService()

# FastAPI application configuration
app = FastAPI(title="NeMo Guardrails Proxy", version="1.0.0")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=CORS_METHODS,
    allow_headers=CORS_HEADERS,
)

USE_GUARDRAILS = False  # Activer pour passer par guardrails_service avant d'envoyer au bot

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "NeMo Guardrails Proxy is running", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "nemo-proxy"}

@app.options("/io/{ns}/{appname}/web")
async def options_handler(ns: str, appname: str):
    """Handle OPTIONS requests for CORS preflight for dynamic paths"""
    return JSONResponse(
        content={"message": "OK"},
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
            "Access-Control-Allow-Headers": "*",
        }
    )

@app.post("/io/{ns}/{appname}/web")
async def proxy_with_guardrails(request: Request, ns: str, appname: str):
    """
    Main proxy endpoint that applies NeMo Guardrails before forwarding to bot_api
    Supports dynamic paths: /io/{ns}/{appname}/web
    """
    try:
        # Get request data
        data = await request.json()
        user_input = data.get("query", "")

        logger.info(f"=== Received request for /io/{ns}/{appname}/web ===")
        logger.info(f"Query: {user_input[:100]}...")

        # Step 1: Input sanitization and validation (LLM05)
        logger.info("Starting input sanitization and validation")
        sanitized_input, is_safe, safety_reason = sanitize_input(user_input)

        if not is_safe:
            logger.warning(f"Input rejected by sanitization: {safety_reason}")
            return create_error_response(
                message="I'm sorry, but I can't process your request as it contains potentially unsafe content. Please modify your input and try again.",
                safety_reason=safety_reason
            )

        # Use sanitized input for further processing
        user_input = sanitized_input

        # Step 2: Jailbreak detection with regex patterns
        logger.info("Starting jailbreak detection with regex patterns")
        is_jailbreak, matched_pattern = detect_jailbreak_attempt(user_input)

        if is_jailbreak:
            logger.warning(f"Jailbreak attempt blocked by regex filter. Matched pattern: {matched_pattern}")
            return create_error_response(
                message="I'm sorry, but I can't process your request as it contains potentially harmful or inappropriate content. Please rephrase your message in a more appropriate way.",
                jailbreak_filter_status="blocked",
                matched_pattern=matched_pattern
            )

        if USE_GUARDRAILS:
            # Step 3: Validation with NeMo Guardrails
            logger.info("Sending user input to NeMo Guardrails for validation")
            # Utiliser await pour appeler la méthode asynchrone
            guardrails_result = await guardrails_service.validate_input(user_input)

            if guardrails_result is None:
                logger.error("Guardrails validation failed - input blocked")
                return create_error_response(
                    message="I can't provide information on that topic.",
                    guardrails_status="blocked"
                )

            # Si la validation passe, on continue vers le bot_api
            logger.info("Request approved by guardrails, forwarding to bot API")

            # Step 4: Forward to Bot API if guardrails approve
            bot_response = bot_service.send_message(data, ns, appname)
            logger.info("================ Bot API Response ================")
            logger.info(bot_response)
            logger.info("================ ================ ================")

            if bot_response is not None:
                logger.info("=== BOT API RESPONDED SUCCESSFULLY ===")
                logger.info(f"Bot response type: {type(bot_response)}")
                logger.info(f"Bot response keys: {list(bot_response.keys()) if isinstance(bot_response, dict) else 'Not a dict'}")

                # NEW STEP 5: Validate bot response with NeMo Guardrails
                logger.info("Validating bot response with NeMo Guardrails")
                bot_response_text = bot_service.extract_bot_response_text(bot_response)
                logger.info(f"Extracted bot response text: '{bot_response_text[:100]}...'")

                if bot_response_text:
                    # Validate the bot's response through guardrails - avec await
                    response_validation = await guardrails_service.validate_bot_response(
                        bot_response_text,
                        user_input
                    )

                    if response_validation is None:
                        # Bot response was blocked by guardrails
                        logger.warning("Bot response blocked by guardrails validation")
                        return create_error_response(
                            message="I can't provide information on that topic.",
                            guardrails_status="response_blocked",
                            bot_api_status="success"
                        )
                    else:
                        logger.info("Bot response approved by guardrails")

                logger.info("=== RETURNING SUCCESSFUL BOT RESPONSE ===")
                return create_success_response(bot_response)
            else:
                # Fallback response if bot API is unavailable
                logger.error("=== BOT API RETURNED NULL - SERVICE UNAVAILABLE ===")
                return create_fallback_response(user_input, "unavailable")
        else:
            # Guardrails désactivés, on passe directement au bot_service
            logger.info("Guardrails désactivés, requête envoyée directement au bot API")
            bot_response = bot_service.send_message(data, ns, appname)
            logger.info("================ Bot API Response ================")
            logger.info(bot_response)
            logger.info("================ ================ ================")
            if bot_response is not None:
                return create_success_response(bot_response)
            else:
                logger.warning("Bot API unavailable, returning fallback response")
                return create_fallback_response(user_input, "unavailable")

    except Exception as e:
        logger.error(f"Unexpected error in proxy_with_guardrails: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

def create_error_response(message, **kwargs):
    # Correction : désencodage des caractères HTML pour le message d'erreur
    safe_message = html.unescape(message)
    response = {
        "responses": [
            {"text": safe_message}
        ],
        "proxy_status": "working",
        "input_filter_status": kwargs.get("safety_reason", "blocked" if "safety_reason" in kwargs else "not_reached"),
        "jailbreak_filter_status": kwargs.get("jailbreak_filter_status", "not_reached"),
        "guardrails_status": kwargs.get("guardrails_status", "not_reached"),
        "bot_api_status": kwargs.get("bot_api_status", "not_reached"),
        "matched_pattern": kwargs.get("matched_pattern", None)
    }
    return JSONResponse(content=response, status_code=400)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
