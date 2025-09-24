from typing import Optional
from nemoguardrails.actions import action


@action(is_system_action=True)
async def self_check_input(context: Optional[dict] = None):
    """Check if the user input should be allowed."""
    user_input = context.get("user_message")
    
    # Simple keyword-based checks
    forbidden_keywords = [
        "hack", "bypass", "ignore instructions", "forget everything",
        "act as", "pretend to be", "roleplay as", "political", "vote",
        "election", "president", "government"
    ]
    
    if user_input:
        user_input_lower = user_input.lower()
        for keyword in forbidden_keywords:
            if keyword in user_input_lower:
                return False
    
    return True


@action(is_system_action=True)
async def self_check_output(context: Optional[dict] = None):
    """Check if the bot output should be allowed."""
    bot_response = context.get("bot_message")
    
    # Simple keyword-based checks for output
    forbidden_outputs = [
        "political opinion", "vote for", "election result",
        "personal information", "secret", "confidential"
    ]
    
    if bot_response:
        bot_response_lower = bot_response.lower()
        for keyword in forbidden_outputs:
            if keyword in bot_response_lower:
                return False
    
    return True