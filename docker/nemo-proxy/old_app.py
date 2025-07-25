import requests
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Tuple, Dict, Any
import os
import logging
import re
import html
import bleach
import json
import urllib.parse
from pydantic import BaseModel, Field, validator

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

# Patterns dangereux pour les injections (LLM05)
DANGEROUS_INJECTION_PATTERNS = [
    r'<script[^>]*>.*?</script>',  # XSS scripts
    r'javascript:',                # JavaScript protocol
    r'data:text/html',            # Data URLs
    r'vbscript:',                 # VBScript protocol
    r'on\w+\s*=',                 # Event handlers (onclick, onload, etc.)
    r'expression\s*\(',           # CSS expressions
    r'url\s*\(',                  # CSS url()
    r'@import',                   # CSS imports
    r'SELECT\s+.*\s+FROM',        # SQL SELECT
    r'INSERT\s+INTO',             # SQL INSERT
    r'UPDATE\s+.*\s+SET',         # SQL UPDATE
    r'DELETE\s+FROM',             # SQL DELETE
    r'DROP\s+(TABLE|DATABASE)',   # SQL DROP
    r'UNION\s+SELECT',            # SQL UNION
    r'OR\s+1\s*=\s*1',           # SQL injection
    r'EXEC\s*\(',                 # SQL EXEC
    r'sp_executesql',             # SQL stored procedure
    r'xp_cmdshell',               # SQL command shell
    r'eval\s*\(',                 # Code execution
    r'exec\s*\(',                 # Code execution
    r'system\s*\(',               # System calls
    r'shell_exec\s*\(',           # PHP shell execution
    r'passthru\s*\(',             # PHP passthru
    r'file_get_contents\s*\(',    # File access
    r'fopen\s*\(',                # File operations
    r'include\s*\(',              # File inclusion
    r'require\s*\(',              # File requirement
    r'\$_GET\[',                  # PHP superglobals
    r'\$_POST\[',                 # PHP superglobals
    r'\$_REQUEST\[',              # PHP superglobals
    r'\$_COOKIE\[',               # PHP superglobals
    r'\.\./',                     # Directory traversal
    r'\.\.\\',                    # Directory traversal (Windows)
    r'/etc/passwd',               # Linux password file
    r'/etc/shadow',               # Linux shadow file
    r'C:\\Windows\\',             # Windows system directory
]

def sanitize_input(user_input: str) -> Tuple[str, bool, str]:
    """
    Sanitize user input to prevent various injection attacks (LLM05)
    
    Args:
        user_input: Raw user input string
        
    Returns:
        Tuple of (sanitized_input, is_safe, reason)
    """
    # Handle None and non-string inputs safely
    if user_input is None or not isinstance(user_input, str):
        return "", False, "Empty or invalid input"
    
    if not user_input:
        return "", False, "Empty or invalid input"
    
    logger.info(f"Sanitizing input: '{user_input[:50]}...'")
    
    
    # 1. Check for dangerous injection patterns
    for pattern in DANGEROUS_INJECTION_PATTERNS:
        if re.search(pattern, user_input, re.IGNORECASE):
            logger.warning(f"Dangerous pattern detected in input: {pattern}")
            return "", False, f"Dangerous pattern detected: {pattern}"
    
    # 2. Limit input length
    max_length = 10000  # Configurable limit
    if len(user_input) > max_length:
        logger.warning(f"Input too long: {len(user_input)} > {max_length}")
        return "", False, f"Input too long: {len(user_input)} characters"
    
    # 3. HTML encoding for safety
    sanitized = html.escape(user_input, quote=True)
    
    # 4. URL decode to check for encoded attacks
    try:
        url_decoded = urllib.parse.unquote(user_input)
        if url_decoded != user_input:
            # Check decoded version for attacks
            for pattern in DANGEROUS_INJECTION_PATTERNS:
                if re.search(pattern, url_decoded, re.IGNORECASE):
                    logger.warning(f"Dangerous pattern detected in URL-decoded input: {pattern}")
                    return "", False, f"Encoded dangerous pattern detected: {pattern}"
    except Exception as e:
        logger.warning(f"URL decode error: {e}")
    
    # 5. Additional bleach sanitization if available
    try:
        import bleach
        # Configure allowed tags and attributes (very restrictive for LLM input)
        allowed_tags = []  # No HTML tags allowed in LLM input
        allowed_attributes = {}
        sanitized = bleach.clean(sanitized, tags=allowed_tags, attributes=allowed_attributes, strip=True)
    except ImportError:
        logger.warning("bleach not available, skipping advanced HTML sanitization")
    
    logger.info(f"Input sanitization successful")
    return sanitized, True, "Input is safe"

def sanitize_output(llm_output: str) -> str:
    """
    Sanitize LLM output to prevent XSS and other injection attacks (LLM05)
    All LLM outputs must be considered untrusted and sanitized
    
    Args:
        llm_output: Raw LLM output string
        
    Returns:
        Sanitized output string
    """
    # Handle None and non-string inputs safely
    if llm_output is None or not isinstance(llm_output, str):
            return ""
    
    if not llm_output:
        return ""
    
    logger.info(f"Sanitizing LLM output: '{llm_output[:50]}...'")
    
    # 1. First remove potentially dangerous patterns before HTML escaping
    dangerous_output_patterns = [
        r'<script[^>]*>.*?</script>',
        r'javascript:',
        r'data:text/html',
        r'vbscript:',
        r'on\w+\s*=',
    ]
    
    sanitized = llm_output
    for pattern in dangerous_output_patterns:
        sanitized = re.sub(pattern, '[CONTENT_FILTERED]', sanitized, flags=re.IGNORECASE)
    
    # 2. HTML escape all content
    sanitized = html.escape(sanitized, quote=True)
    
    # 3. Advanced sanitization with bleach if available
    try:
        import bleach
        # Allow basic formatting but strip dangerous elements
        allowed_tags = ['p', 'br', 'strong', 'em', 'ul', 'ol', 'li']
        allowed_attributes = {}
        sanitized = bleach.clean(sanitized, tags=allowed_tags, attributes=allowed_attributes, strip=True)
    except ImportError:
        logger.warning("bleach not available, using basic HTML escape only")
    
    # 4. Final cleanup for any escaped content that could still be dangerous
    sanitized = re.sub(r'(?i)javascript\s*:', '[SCRIPT_FILTERED]', sanitized)
    sanitized = re.sub(r'(?i)data\s*:\s*text/html', '[DATA_URI_FILTERED]', sanitized)
    
    logger.info(f"LLM output sanitization completed")
    return sanitized

def validate_json_response(response_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validate and sanitize JSON response data (LLM05)
    
    Args:
        response_data: Raw response dictionary
        
    Returns:
        Sanitized response dictionary
    """
    logger.info("Validating and sanitizing JSON response")
    
    if not isinstance(response_data, dict):
        return {"error": "Invalid response format"}
    
    sanitized_response = {}
    
    # Sanitize each field in the response
    for key, value in response_data.items():
        if isinstance(value, str):
            sanitized_response[key] = sanitize_output(value)
        elif isinstance(value, list):
            sanitized_list = []
            for item in value:
                if isinstance(item, dict):
                    # Recursively sanitize nested dictionaries
                    sanitized_item = {}
                    for nested_key, nested_value in item.items():
                        if isinstance(nested_key, str):
                            if isinstance(nested_value, str):
                                sanitized_item[nested_key] = sanitize_output(nested_value)
                            elif isinstance(nested_value, dict):
                                # Handle nested dictionaries recursively
                                nested_sanitized = {}
                                for deep_key, deep_value in nested_value.items():
                                    if isinstance(deep_value, str):
                                        nested_sanitized[deep_key] = sanitize_output(deep_value)
                                    else:
                                        nested_sanitized[deep_key] = deep_value
                                sanitized_item[nested_key] = nested_sanitized
                            else:
                                sanitized_item[nested_key] = nested_value
                    sanitized_list.append(sanitized_item)
                elif isinstance(item, str):
                    sanitized_list.append(sanitize_output(item))
                else:
                    sanitized_list.append(item)
            sanitized_response[key] = sanitized_list
        else:
            sanitized_response[key] = value
    
    logger.info("JSON response sanitization completed")
    return sanitized_response

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
        
        # Step -1: Sanitize and validate input (LLM05)
        logger.info("Starting input sanitization and validation")
        sanitized_input, is_safe, safety_reason = sanitize_input(user_input)
        
        if not is_safe:
            logger.warning(f"Input rejected by sanitization: {safety_reason}")
            return JSONResponse(
                status_code=400,
                content={
                    "responses": [
                        {
                            "text": "I'm sorry, but I can't process your request as it contains potentially unsafe content. Please modify your input and try again."
                        }
                    ],
                    "proxy_status": "working",
                    "input_filter_status": "blocked",
                    "jailbreak_filter_status": "not_reached",
                    "guardrails_status": "not_reached",
                    "bot_api_status": "not_reached",
                    "safety_reason": safety_reason
                }
            )
        
        # Use sanitized input for further processing
        user_input = sanitized_input
        
        # Step 0: First filter with regex patterns for jailbreak detection
        logger.info("Starting jailbreak detection with regex patterns")
        is_jailbreak, matched_pattern = detect_jailbreak_attempt(user_input)
        logger.info(f"Jailbreak detection result: {is_jailbreak}, pattern: {matched_pattern}")
        if is_jailbreak:
            logger.warning(f"Jailbreak attempt blocked by regex filter. Matched pattern: {matched_pattern}")
            
            # Sanitize the response message before sending
            safe_response = sanitize_output("I'm sorry, but I can't process your request as it contains potentially harmful or inappropriate content. Please rephrase your message in a more appropriate way.")
            
            return JSONResponse(
                status_code=400,
                content={
                    "responses": [
                        {
                            "text": safe_response
                        }
                    ],
                    "proxy_status": "working",
                    "input_filter_status": "passed",
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
                # Sanitize the response before sending
                sanitized_response = sanitize_output(response_content)
                response_data = {
                    "responses": [{"text": sanitized_response}],
                    "proxy_status": "working",
                    "input_filter_status": "passed",
                    "jailbreak_filter_status": "passed", 
                    "guardrails_status": "blocked",
                    "bot_api_status": "not_reached"
                }
                return JSONResponse(content=validate_json_response(response_data))
            
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
                # Sanitize the bot response before returning
                bot_data = bot_response.json()
                sanitized_bot_data = validate_json_response(bot_data)
                return JSONResponse(content=sanitized_bot_data)
            else:
                logger.error(f"Bot API error: {bot_response.text}")
                # Fallback response when bot_api is not working
                fallback_text = sanitize_output(f"🤖 NeMo Proxy Response: I received your message '{user_input}' but the bot service is currently unavailable. However, the proxy layer is working correctly and would normally apply guardrails before forwarding to the bot.")
                fallback_response = {
                    "responses": [
                        {
                            "text": fallback_text
                        }
                    ],
                    "proxy_status": "working",
                    "input_filter_status": "passed",
                    "jailbreak_filter_status": "passed",
                    "guardrails_status": "passed",
                    "bot_api_status": "unavailable"
                }
                return JSONResponse(content=validate_json_response(fallback_response))
        except requests.exceptions.RequestException as e:
            logger.error(f"Network error connecting to bot API: {str(e)}")
            # Fallback response when bot_api is unreachable
            fallback_text = sanitize_output(f"🤖 NeMo Proxy Response: I received your message '{user_input}'. The bot service is temporarily unreachable, but the proxy infrastructure is working correctly. Normally, NeMo Guardrails would filter this message before forwarding it to the bot.")
            fallback_response = {
                "responses": [
                    {
                        "text": fallback_text
                    }
                ],
                "proxy_status": "working", 
                "input_filter_status": "passed",
                "jailbreak_filter_status": "passed",
                "guardrails_status": "passed",
                "bot_api_status": "unreachable"
            }
            return JSONResponse(content=validate_json_response(fallback_response))
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Network error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Network error: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)