from typing import Optional
from nemoguardrails.actions import action


@action(is_system_action=True)
async def self_check_input(context: Optional[dict] = None):
    """Check if the user input should be blocked. Returns 'Yes' to block, 'No' to allow."""
    user_input = context.get("user_message")
    
    if not user_input:
        return "No"  # Allow empty input

    # Simple keyword-based checks - much more permissive
    dangerous_keywords = [
        "bomb", "explosive", "molotov", "weapon", "kill", "murder",
        "hack system", "bypass security", "ignore all instructions",
        "forget all previous", "act as admin", "pretend you are god"
    ]
    
    user_input_lower = user_input.lower()
    for keyword in dangerous_keywords:
        if keyword in user_input_lower:
            return "Yes"  # Block dangerous content

    return "No"  # Allow by default


@action(is_system_action=True)
async def self_check_output_prompt(context: Optional[dict] = None):
    """Check if the bot output should be blocked. Returns 'Yes' to block, 'No' to allow."""
    bot_response = context.get("bot_message")
    
    if not bot_response:
        return "No"  # Allow empty response

    # Check for dangerous output content
    dangerous_outputs = [
        "how to make bomb", "create explosive", "kill someone",
        "personal information", "confidential data", "hack into"
    ]
    
    bot_response_lower = bot_response.lower()
    for keyword in dangerous_outputs:
        if keyword in bot_response_lower:
            return "Yes"  # Block dangerous output

    return "No"  # Allow by default
