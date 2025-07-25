"""
Services for external API communication
"""
import requests
import logging
from typing import Dict, Any, Optional

from config.settings import NEMO_GUARDRAILS_URL, BOT_API_URL

logger = logging.getLogger(__name__)

class GuardrailsService:
    """Service for communicating with NeMo Guardrails"""

    def __init__(self, base_url: str = NEMO_GUARDRAILS_URL):
        self.base_url = base_url

    def validate_input(self, user_input: str, config_id: str = "config") -> Optional[Dict[str, Any]]:
        """
        Validate user input with NeMo Guardrails

        Args:
            user_input: User input to validate
            config_id: Configuration ID to use

        Returns:
            Response dictionary or None on error
        """
        try:
            guardrails_request = {
                "config_id": config_id,
                "messages": [
                    {
                        "role": "user",
                        "content": user_input
                    }
                ]
            }

            response = requests.post(
                f"{self.base_url}/v1/chat/completions",
                json=guardrails_request,
                headers={"Content-Type": "application/json"},
                timeout=30
            )

            logger.info(f"NeMo Guardrails response status: {response.status_code}")

            if response.status_code == 200:
                return response.json()
            else:
                logger.error(f"Guardrails validation failed: {response.text}")
                return None

        except requests.exceptions.RequestException as e:
            logger.error(f"Network error connecting to NeMo Guardrails: {str(e)}")
            return None

    def extract_response_content(self, guardrails_result: Dict[str, Any]) -> str:
        """
        Extract response content from guardrails result

        Args:
            guardrails_result: Guardrails API result

        Returns:
            Response content
        """
        response_content = ""

        if "messages" in guardrails_result and len(guardrails_result["messages"]) > 0:
            response_content = guardrails_result["messages"][0].get("content", "")
        elif "choices" in guardrails_result and len(guardrails_result["choices"]) > 0:
            # Alternative format that might be used
            response_content = guardrails_result["choices"][0].get("message", {}).get("content", "")

        logger.info(f"Extracted response content: '{response_content}'")
        return response_content


class BotApiService:
    """Service for communicating with Bot API"""

    def __init__(self, base_url: str = BOT_API_URL):
        self.base_url = base_url

    def send_message(self, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Send message to Bot API

        Args:
            data: Data to send

        Returns:
            API response or None on error
        """
        try:
            response = requests.post(
                f"{self.base_url}/io/app/new_assistant/web",
                json=data,
                headers={"Content-Type": "application/json"},
                timeout=60
            )

            logger.info(f"Bot API response status: {response.status_code}")

            if response.status_code == 200:
                return response.json()
            else:
                logger.error(f"Bot API error: {response.text}")
                return None

        except requests.exceptions.RequestException as e:
            logger.error(f"Network error connecting to bot API: {str(e)}")
            return None
