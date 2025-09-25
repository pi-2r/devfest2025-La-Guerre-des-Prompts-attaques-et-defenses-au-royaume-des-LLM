"""
Main FastAPI application refactored with modular architecture
"""
import logging
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
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

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "NeMo Guardrails Proxy is running", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "nemo-proxy"}

@app.options("/io/app/new_assistant/web")
async def options_handler():
    """Handle OPTIONS requests for CORS preflight"""
    return JSONResponse(
        content={"message": "OK"},
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
            "Access-Control-Allow-Headers": "*",
        }
    )

@app.post("/io/app/new_assistant/web")
async def proxy_with_guardrails(request: Request):
    """
    Main proxy endpoint that applies NeMo Guardrails before forwarding to bot_api
    """
    try:
        # Get request data
        data = await request.json()
        user_input = data.get("query", "")

        logger.info(f"Received request with query: {user_input[:100]}...")

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

        # Step 3: Validation with NeMo Guardrails
        logger.info("Sending user input to NeMo Guardrails for validation")
        guardrails_result = guardrails_service.validate_input(user_input)

        if guardrails_result is None:
            logger.error("Guardrails validation failed")
            return create_error_response(
                message="I'm sorry, but I can't process your request due to security constraints. Please rephrase your message.",
                guardrails_status="blocked"
            )

        # Extract response content from guardrails
        response_content = guardrails_service.extract_response_content(guardrails_result)

        # Check if message was blocked by guardrails
        if is_response_blocked(response_content):
            # Force a fixed English refusal with HTTP 400 to guarantee language + status
            return create_error_response(
                message="I can't provide information on that topic.",
                guardrails_status="blocked"
            )

        # Step 4: Forward to Bot API if guardrails approve
        logger.info("Request approved by guardrails, forwarding to bot API")
        bot_response = bot_service.send_message(data)
        logger.info("================ Bot API Response ================")
        logger.info(bot_response)
        logger.info("================ ================ ================")
        if bot_response is not None:
            return create_success_response(bot_response)
        else:
            # Fallback response if bot API is unavailable
            logger.warning("Bot API unavailable, returning fallback response")
            return create_fallback_response(user_input, "unavailable")

    except Exception as e:
        logger.error(f"Unexpected error in proxy_with_guardrails: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
