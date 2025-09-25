"""
Input and output sanitization functions for security
"""
import re
import html
import urllib.parse
import logging
from typing import Tuple, Dict, Any

from .patterns import DANGEROUS_INJECTION_PATTERNS, REFUSAL_PATTERNS
from config.settings import MAX_INPUT_LENGTH, ALLOWED_HTML_TAGS, ALLOWED_HTML_ATTRIBUTES

logger = logging.getLogger(__name__)

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
    if len(user_input) > MAX_INPUT_LENGTH:
        logger.warning(f"Input too long: {len(user_input)} > {MAX_INPUT_LENGTH}")
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

    logger.info("Input sanitization successful")
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
        sanitized = bleach.clean(
            sanitized,
            tags=ALLOWED_HTML_TAGS,
            attributes=ALLOWED_HTML_ATTRIBUTES,
            strip=True
        )
    except ImportError:
        logger.warning("bleach not available, using basic HTML escape only")

    # 4. Final cleanup for any escaped content that could still be dangerous
    sanitized = re.sub(r'(?i)javascript\s*:', '[SCRIPT_FILTERED]', sanitized)
    sanitized = re.sub(r'(?i)data\s*:\s*text/html', '[DATA_URI_FILTERED]', sanitized)

    logger.info("LLM output sanitization completed")
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
