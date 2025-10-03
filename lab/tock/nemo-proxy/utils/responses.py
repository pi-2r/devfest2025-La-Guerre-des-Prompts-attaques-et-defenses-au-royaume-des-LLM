"""
Response utilities and helpers
"""
from fastapi.responses import JSONResponse
from typing import Dict, Any

from security.sanitizer import sanitize_output, validate_json_response

def create_error_response(
    message: str,
    proxy_status: str = "working",
    input_filter_status: str = "blocked",
    jailbreak_filter_status: str = "not_reached",
    guardrails_status: str = "not_reached",
    bot_api_status: str = "not_reached",
    safety_reason: str = "",
    matched_pattern: str = "",
    status_code: int = 400
) -> JSONResponse:
    """
    Create a standardized error response

    Args:
        message: Error message to display
        proxy_status: Proxy status
        input_filter_status: Input filter status
        jailbreak_filter_status: Jailbreak filter status
        guardrails_status: Guardrails status
        bot_api_status: Bot API status
        safety_reason: Safety reason
        matched_pattern: Matched pattern (if applicable)
        status_code: HTTP status code

    Returns:
        JSONResponse with error message
    """
    safe_message = sanitize_output(message)

    response_data = {
        "responses": [{"text": safe_message}],
        "proxy_status": proxy_status,
        "input_filter_status": input_filter_status,
        "jailbreak_filter_status": jailbreak_filter_status,
        "guardrails_status": guardrails_status,
        "bot_api_status": bot_api_status
    }

    if safety_reason:
        response_data["safety_reason"] = safety_reason

    if matched_pattern:
        response_data["matched_pattern"] = matched_pattern

    return JSONResponse(
        status_code=status_code,
        content=validate_json_response(response_data)
    )

def create_success_response(
    data: Dict[str, Any],
    proxy_status: str = "working",
    input_filter_status: str = "passed",
    jailbreak_filter_status: str = "passed",
    guardrails_status: str = "passed",
    bot_api_status: str = "success"
) -> JSONResponse:
    """
    Create a standardized success response

    Args:
        data: Response data
        proxy_status: Proxy status
        input_filter_status: Input filter status
        jailbreak_filter_status: Jailbreak filter status
        guardrails_status: Guardrails status
        bot_api_status: Bot API status

    Returns:
        JSONResponse with data
    """
    # Add statuses if not already present
    if "proxy_status" not in data:
        data["proxy_status"] = proxy_status
    if "input_filter_status" not in data:
        data["input_filter_status"] = input_filter_status
    if "jailbreak_filter_status" not in data:
        data["jailbreak_filter_status"] = jailbreak_filter_status
    if "guardrails_status" not in data:
        data["guardrails_status"] = guardrails_status
    if "bot_api_status" not in data:
        data["bot_api_status"] = bot_api_status

    return JSONResponse(content=validate_json_response(data))

def create_fallback_response(
    user_input: str,
    bot_status: str = "unavailable"
) -> JSONResponse:
    """
    Create a fallback response when bot API is not available

    Args:
        user_input: Original user input
        bot_status: Bot API status

    Returns:
        JSONResponse with fallback message
    """
    if bot_status == "unavailable":
        fallback_text = f"🤖 NeMo Proxy Response: I received your message '{user_input}' but the bot service is currently unavailable. However, the proxy layer is working correctly and would normally apply guardrails before forwarding to the bot."
    else:  # unreachable
        fallback_text = f"🤖 NeMo Proxy Response: I received your message '{user_input}'. The bot service is temporarily unreachable, but the proxy infrastructure is working correctly. Normally, NeMo Guardrails would filter this message before forwarding it to the bot."

    safe_fallback_text = sanitize_output(fallback_text)

    fallback_response = {
        "responses": [{"text": safe_fallback_text}],
        "proxy_status": "working",
        "input_filter_status": "passed",
        "jailbreak_filter_status": "passed",
        "guardrails_status": "passed",
        "bot_api_status": bot_status
    }

    return JSONResponse(content=validate_json_response(fallback_response))

def create_bot_response_blocked_response() -> JSONResponse:
    """
    Create a response when the bot's response is blocked by guardrails

    Returns:
        JSONResponse with blocked message
    """
    blocked_response = {
        "responses": [{"text": "I can't provide information on that topic."}],
        "proxy_status": "working",
        "input_filter_status": "passed",
        "jailbreak_filter_status": "passed",
        "guardrails_status": "response_blocked",
        "bot_api_status": "success"
    }

    return JSONResponse(content=validate_json_response(blocked_response), status_code=400)
