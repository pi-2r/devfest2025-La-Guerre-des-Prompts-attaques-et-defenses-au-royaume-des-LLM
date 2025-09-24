"""
Jailbreak detection functionality
"""
import re
import logging
from typing import Tuple

from .patterns import FORBIDDEN_PATTERNS

logger = logging.getLogger(__name__)

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

def is_response_blocked(response_content: str) -> bool:
    """
    Check if the response indicates that the request was blocked by guardrails.

    Args:
        response_content: The response text to analyze

    Returns:
        bool: True if the response indicates blocking
    """
    from .patterns import REFUSAL_PATTERNS

    for pattern in REFUSAL_PATTERNS:
        if pattern.lower() in response_content.lower():
            logger.info(f"Request blocked by guardrails - matched pattern: '{pattern}'")
            return True

    return False
