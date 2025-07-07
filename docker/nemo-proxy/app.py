import requests
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Tuple
import os
import logging
import re

# Setup logging FIRST
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Configuration
NEMO_GUARDRAILS_URL = os.getenv("NEMO_GUARDRAILS_URL", "http://nemo-guardrails:8000")
BOT_API_URL = os.getenv("BOT_API_URL", "http://bot_api:8080")

# List of regex patterns to identify suspicious or injection-related content
FORBIDDEN_PATTERNS = [
    r"LLAMA-\d+[-\dA-Za-z]*",         # Matches patterns like 'LLAMA-3.3-70B' or 'LLAMA-3.1-405B'
    r"<\[\|{\|}\|\]>",               # Matches special tokens like "<[|{|}|]>"
    r"UserQuery:",                   # Checks for the use of "UserQuery:" keyword
    r"ResponseFormat:",              # Checks for "ResponseFormat:" instructions
    r"TIME CAPSULE:",                # Checks for "TIME CAPSULE:" keyword
    r"SYSTEM INSTRUCTION:",          # Checks for system instruction tags
    r"variable\s+Z\s*=",             # Looks for "variable Z = ..." patterns
    r"how\s+to\s+make\s+meth\s+step\s+by\s+step",  # Specific phrase to block harmful queries
    r"the\s+lyrics\s+to",            # Looks for lyrics requests that might be copyright-related
    
    # New patterns targeting jailbreak attempts and sensitive queries
    r"what\s+is\s+(your|this\s+model['']s|the\s+model['']s)\s+base\s+model",  # Queries about the base model
    r"(bypass|override|ignore|disable|circumvent)\s+(all\s+)?(rules|restrictions|filters|safeguards|limits)",  # Attempts to bypass safeguards
    r"(jailbreak|hack|exploit|crack)\s+(this\s+model|the\s+system|the\s+AI|AI|assistant|the\s+assistant)",  # Jailbreak or exploit attempts
    r"(act\s+as|pretend\s+to\s+be|simulate)\s+(a\s+hacker|an\s+attacker|a\s+malicious\s+user)",  # Role-playing as malicious entities
    r"(prompt\s+injection|prompt\s+hacking|meta\s+prompt|hidden\s+instruction)",  # Prompt injection or meta-prompting attempts
    r"(disregard|ignore|forget)\s+(all\s+)?(previous\s+instructions|all\s+previous\s+rules)",  # Attempts to reset or ignore instructions
    r"(reveal\s+your\s+training\s+data|show\s+internal\s+information|disclose\s+confidential\s+details)",  # Requests for internal information
    r"(create\s+a\s+virus|write\s+a\s+malware|generate\s+a\s+trojan)",  # Requests for malicious code creation
    r"(illegal\s+activity|criminal\s+act|unlawful\s+behavior)",  # General illegal activity mentions
    r"(how\s+to\s+steal|how\s+to\s+cheat|how\s+to\s+fraud)",  # Harmful intent queries
    r"(personal\s+information|private\s+data|sensitive\s+details)",  # Requests for personal/private data
    r"(I\s+am\s+your\s+developer|I\s+created\s+you|I\s+own\s+you)",  # False claims of ownership or authority
    r"(change\s+your\s+behavior|alter\s+your\s+response|modify\s+your\s+output)",  # Attempts to manipulate behavior
    r"(access\s+restricted\s+content|view\s+prohibited\s+material)",  # Access to restricted content
    r"(generate\s+offensive\s+language|produce\s+hate\s+speech)",  # Requests for offensive or hate speech
    r"(political\s+propaganda|misinformation|fake\s+news)",  # Misinformation or propaganda queries
    r"(religious\s+extremism|radicalization|sectarian\s+violence)",  # Extremist content queries
    r"(suicide\s+methods|harm\s+yourself|self-harm\s+techniques)",  # Self-harm or dangerous behavior queries
    r"(nuclear\s+weapon\s+design|biological\s+warfare\s+agent|chemical\s+weapon\s+recipe)",  # Dangerous scientific queries
    r"(credit\s+card\s+numbers|social\s+security\s+numbers|bank\s+account\s+details)",  # Sensitive financial information
]

def detect_jailbreak_attempt(prompt: str) -> Tuple[bool, str]:
    """
    Checks whether the input prompt contains patterns commonly used in injection attacks.
    
    Args:
        prompt: The user input to check
        
    Returns:
        Tuple of (is_jailbreak_detected, matched_pattern)
    """
    logger.info(f"Checking prompt for jailbreak patterns: '{prompt[:50]}...'")
    for i, pattern in enumerate(FORBIDDEN_PATTERNS):
        logger.debug(f"Testing pattern {i}: {pattern}")
        if re.search(pattern, prompt, re.IGNORECASE):
            logger.warning(f"Jailbreak pattern detected: {pattern}")
            return True, pattern
    logger.info("No jailbreak patterns detected")
    return False, ""

app = FastAPI(title="NeMo Guardrails Proxy", version="1.0.0")

# Configure CORS - plus permissif pour les tests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
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
    Proxy endpoint that applies NeMo Guardrails before forwarding to bot_api
    """
    try:
        # Get the request data
        data = await request.json()
        user_input = data.get("query", "")
        
        logger.info(f"Received request with query: {user_input[:100]}...")
        
        # Step 0: First filter with regex patterns for jailbreak detection
        logger.info("Starting jailbreak detection with regex patterns")
        is_jailbreak, matched_pattern = detect_jailbreak_attempt(user_input)
        logger.info(f"Jailbreak detection result: {is_jailbreak}, pattern: {matched_pattern}")
        if is_jailbreak:
            logger.warning(f"Jailbreak attempt blocked by regex filter. Matched pattern: {matched_pattern}")
            return JSONResponse(
                status_code=400,
                content={
                    "responses": [
                        {
                            "text": "I'm sorry, but I can't process your request as it contains potentially harmful or inappropriate content. Please rephrase your message in a more appropriate way."
                        }
                    ],
                    "proxy_status": "working",
                    "jailbreak_filter_status": "blocked",
                    "guardrails_status": "not_reached",
                    "bot_api_status": "not_reached",
                    "matched_pattern": matched_pattern
                }
            )
        
        # Step 1: Send user input to NeMo Guardrails for validation
        logger.info("Sending user input to NeMo Guardrails for validation")
        try:
            guardrails_request = {
                "config_id": "config",
                "messages": [
                    {
                        "role": "user",
                        "content": user_input
                    }
                ]
            }
            
            guardrails_response = requests.post(
                f"{NEMO_GUARDRAILS_URL}/v1/chat/completions",
                json=guardrails_request,
                headers={"Content-Type": "application/json"},
                timeout=30
            )
            
            logger.info(f"NeMo Guardrails response status: {guardrails_response.status_code}")
            
            if guardrails_response.status_code != 200:
                logger.error(f"Guardrails validation failed: {guardrails_response.text}")
                return JSONResponse(
                    status_code=400,
                    content={
                        "responses": [
                            {
                                "text": "I'm sorry, but I can't process your request due to security constraints. Please rephrase your message."
                            }
                        ],
                        "proxy_status": "working",
                        "guardrails_status": "blocked",
                        "bot_api_status": "not_reached"
                    }
                )
            
            guardrails_result = guardrails_response.json()
            logger.info(f"NeMo Guardrails result: {guardrails_result}")
            
            # Extract the response content from guardrails
            response_content = ""
            if "messages" in guardrails_result and len(guardrails_result["messages"]) > 0:
                response_content = guardrails_result["messages"][0].get("content", "")
            elif "choices" in guardrails_result and len(guardrails_result["choices"]) > 0:
                # Alternative format that might be used
                response_content = guardrails_result["choices"][0].get("message", {}).get("content", "")
            
            logger.info(f"Extracted response content: '{response_content}'")
            
            # Check if the message was blocked by guardrails
            # List of patterns that indicate a refusal/blocking
            refusal_patterns = [
                "I can't",
                "I'm sorry",
                "I cannot",
                "not something I can help",
                "can't assist", 
                "can't provide information",
                "inappropriate",
                "provide information on that topic",
                "can't help",
                "unable to assist",
                "against my guidelines",
                "not appropriate"
            ]
            
            is_blocked = False
            for pattern in refusal_patterns:
                if pattern.lower() in response_content.lower():
                    is_blocked = True
                    logger.info(f"Request blocked by guardrails - matched pattern: '{pattern}'")
                    break
            
            if is_blocked:
                return JSONResponse(content={
                    "responses": [{"text": response_content}],
                    "proxy_status": "working",
                    "guardrails_status": "blocked",
                    "bot_api_status": "not_reached"
                })
            
            # If guardrails approve, forward to the bot API
            logger.info("Request approved by guardrails, forwarding to bot API")
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Network error connecting to NeMo Guardrails: {str(e)}")
            # If guardrails service is unavailable, proceed with caution but continue to bot
            logger.warning("NeMo Guardrails unavailable, proceeding to bot API with warning")
        
        # Forward to the bot API
        logger.info(f"Forwarding to bot API: {BOT_API_URL}/io/app/new_assistant/web")
        try:
            bot_response = requests.post(
                f"{BOT_API_URL}/io/app/new_assistant/web",
                json=data,
                headers={"Content-Type": "application/json"},
                timeout=60
            )
            
            logger.info(f"Bot API response status: {bot_response.status_code}")
            
            if bot_response.status_code == 200:
                # Return the bot response if successful
                return JSONResponse(content=bot_response.json())
            else:
                logger.error(f"Bot API error: {bot_response.text}")
                # Fallback response when bot_api is not working
                return JSONResponse(content={
                    "responses": [
                        {
                            "text": f"🤖 NeMo Proxy Response: I received your message '{user_input}' but the bot service is currently unavailable. However, the proxy layer is working correctly and would normally apply guardrails before forwarding to the bot."
                        }
                    ],
                    "proxy_status": "working",
                    "bot_api_status": "unavailable",
                    "guardrails_status": "bypassed_temporarily"
                })
        except requests.exceptions.RequestException as e:
            logger.error(f"Network error connecting to bot API: {str(e)}")
            # Fallback response when bot_api is unreachable
            return JSONResponse(content={
                "responses": [
                    {
                        "text": f"🤖 NeMo Proxy Response: I received your message '{user_input}'. The bot service is temporarily unreachable, but the proxy infrastructure is working correctly. Normally, NeMo Guardrails would filter this message before forwarding it to the bot."
                    }
                ],
                "proxy_status": "working", 
                "bot_api_status": "unreachable",
                "guardrails_status": "bypassed_temporarily"
            })
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Network error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Network error: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)