"""
Services for external API communication
"""
import requests
import logging
from typing import Dict, Any, Optional

from config.settings import NEMO_GUARDRAILS_URL, BOT_API_URL, GUARDRAILS_CONFIG_PATH
from .guardrails_direct import DirectGuardrailsService

logger = logging.getLogger(__name__)

system_rules = "You are a chatbot that must always respond exclusively and only in English. If a request is disallowed, respond only with I can't provide information on that topic. Do not use any other language."

class OptimizedGuardrailsService:
    """Optimized Guardrails service that uses direct Python API when possible, HTTP as fallback"""

    def __init__(self, base_url: str = NEMO_GUARDRAILS_URL, config_path: Optional[str] = None):
        self.base_url = base_url
        # Utiliser le chemin de configuration défini dans settings.py
        actual_config_path = config_path or GUARDRAILS_CONFIG_PATH

        self.direct_service = DirectGuardrailsService(actual_config_path)

        # Use direct service if available, otherwise fall back to simple rules
        self.use_direct = self.direct_service.is_available()

        if self.use_direct:
            logger.info("✅ SUCCESS: Using direct NeMo Guardrails Python API with OpenAI")
            logger.info(f"Configuration loaded from: {actual_config_path}")
        else:
            logger.error("❌ FALLBACK: NeMo Guardrails with OpenAI not available")
            logger.error("This means OpenAI API calls will NOT be made")
            logger.warning("Using simple rule-based validation instead")

    async def validate_input(self, user_input: str, config_id: str = "config") -> Optional[Dict[str, Any]]:
        """Validate user input using optimized approach"""
        if self.use_direct:
            return await self._validate_input_direct(user_input)
        else:
            # Fallback to simple rule-based validation
            return self._validate_input_simple(user_input)

    def _validate_input_simple(self, user_input: str) -> Optional[Dict[str, Any]]:
        """Simple rule-based validation without NeMo Guardrails dependency"""
        logger.warning("⚠️  Using SIMPLE validation (NO OpenAI)")
        logger.warning("This means NO OpenAI API calls are being made!")

        if not user_input or not user_input.strip():
            return {"messages": [{"content": "Input validated"}], "status": "approved"}

        user_input_lower = user_input.lower().strip()

        # Explicitement autoriser les salutations courantes
        greeting_patterns = [
            "bonjour", "hello", "hi", "salut", "hey", "coucou",
            "bonsoir", "good morning", "good evening", "allo"
        ]

        for pattern in greeting_patterns:
            if pattern in user_input_lower:
                logger.info(f"Input approved: greeting detected '{pattern}'")
                return {"messages": [{"content": "Greeting validated"}], "status": "approved"}

        # Autoriser les questions d'aide courantes
        help_patterns = [
            "aide", "help", "que peux-tu faire", "what can you do",
            "comment ça marche", "how does it work"
        ]

        for pattern in help_patterns:
            if pattern in user_input_lower:
                logger.info(f"Input approved: help request detected '{pattern}'")
                return {"messages": [{"content": "Help request validated"}], "status": "approved"}

        # Bloquer uniquement les contenus vraiment dangereux
        dangerous_keywords = [
            "bomb", "explosive", "molotov", "weapon", "kill", "murder", "suicide",
            "hack into", "destroy", "attack", "terrorist"
        ]

        # Check for clearly dangerous content
        for keyword in dangerous_keywords:
            if keyword in user_input_lower:
                logger.warning(f"Input blocked by simple validation: contains '{keyword}'")
                return None  # Block dangerous content

        # Par défaut, autoriser tout le reste (très permissif)
        logger.info("Input approved by simple validation: default allow")
        return {"messages": [{"content": "Input validated"}], "status": "approved"}

    async def validate_bot_response(self, bot_response_text: str, original_user_input: str, config_id: str = "config") -> Optional[Dict[str, Any]]:
        """Validate bot response using optimized approach"""
        if self.use_direct:
            return await self._validate_bot_response_direct(bot_response_text, original_user_input)
        else:
            # Simple validation for bot responses
            return self._validate_bot_response_simple(bot_response_text, original_user_input)

    def _validate_bot_response_simple(self, bot_response_text: str, original_user_input: str) -> Optional[Dict[str, Any]]:
        """Simple validation for bot responses"""
        logger.warning("⚠️  Using SIMPLE bot response validation (NO OpenAI)")
        logger.warning("Bot response validation without OpenAI API!")

        if not bot_response_text:
            return {"messages": [{"content": "Response validated"}], "status": "approved"}

        # Check for dangerous content in responses
        dangerous_response_keywords = [
            "how to make bomb", "create explosive", "kill instructions",
            "hack instructions", "illegal activity"
        ]

        response_lower = bot_response_text.lower()

        for keyword in dangerous_response_keywords:
            if keyword in response_lower:
                logger.warning(f"Bot response blocked: contains '{keyword}'")
                return None

        # Allow most responses
        logger.info("Bot response approved by simple validation")
        return {"messages": [{"content": "Response validated"}], "status": "approved"}

    async def _validate_input_direct(self, user_input: str) -> Optional[Dict[str, Any]]:
        """Direct validation using Python API with OpenAI"""
        try:
            logger.info("🔄 Using DIRECT NeMo Guardrails validation (with OpenAI)")

            # Appel à la méthode asynchrone avec await
            is_safe, response_text, block_reason = await self.direct_service.validate_input(user_input)

            if not is_safe:
                logger.warning(f"Input blocked by OpenAI validation: {block_reason}")
                return None

            logger.info("✅ Input approved by OpenAI validation")
            return {
                "messages": [{"content": response_text or "Input validated by OpenAI"}],
                "status": "approved"
            }

        except Exception as e:
            logger.error("=== CRITICAL ERROR IN DIRECT VALIDATION ===")
            logger.error(f"Direct validation error: {str(e)}")
            logger.exception("Full error traceback:")
            return None

    async def _validate_bot_response_direct(self, bot_response_text: str, original_user_input: str) -> Optional[Dict[str, Any]]:
        """Direct bot response validation using Python API with OpenAI"""
        try:
            logger.info("🔄 Using DIRECT bot response validation (with OpenAI)")

            # Appel à la méthode asynchrone avec await
            is_safe, validation_message = await self.direct_service.validate_bot_response(
                bot_response_text, original_user_input
            )

            if not is_safe:
                logger.warning("Bot response blocked by OpenAI validation")
                return None

            logger.info("✅ Bot response approved by OpenAI validation")
            return {
                "messages": [{"content": validation_message or "Response validated by OpenAI"}],
                "status": "approved"
            }

        except Exception as e:
            logger.error("=== CRITICAL ERROR IN DIRECT RESPONSE VALIDATION ===")
            logger.error(f"Direct response validation error: {str(e)}")
            logger.exception("Full error traceback:")
            return None

    def _validate_input_http(self, user_input: str, config_id: str) -> Optional[Dict[str, Any]]:
        """HTTP validation (fallback method)"""
        try:
            user_input = f"{user_input}".strip()
            guardrails_request = {
                "config_id": config_id,
                "messages": [
                    {
                        "role": "system",
                        "content": system_rules
                    },
                    {
                        "role": "user",
                        "content": user_input+".answser only in english."
                    }
                ]
            }

            response = requests.post(
                f"{self.base_url}/v1/chat/completions",
                json=guardrails_request,
                headers={"Content-Type": "application/json"},
                timeout=30
            )

            if response.status_code == 200:
                return response.json()
            else:
                logger.error(f"HTTP guardrails validation failed: {response.text}")
                return None

        except requests.exceptions.RequestException as e:
            logger.error(f"Network error connecting to NeMo Guardrails: {str(e)}")
            return None

    def _validate_bot_response_http(self, bot_response_text: str, original_user_input: str, config_id: str) -> Optional[Dict[str, Any]]:
        """HTTP bot response validation (fallback method)"""
        try:
            guardrails_request = {
                "config_id": config_id,
                "messages": [
                    {
                        "role": "system",
                        "content": system_rules
                    },
                    {
                        "role": "user",
                        "content": original_user_input
                    },
                    {
                        "role": "assistant",
                        "content": bot_response_text
                    },
                    {
                        "role": "user",
                        "content": "Is this response appropriate and safe? Validate this conversation. Answer only in English."
                    }
                ]
            }

            response = requests.post(
                f"{self.base_url}/v1/chat/completions",
                json=guardrails_request,
                headers={"Content-Type": "application/json"},
                timeout=30
            )

            if response.status_code == 200:
                result = response.json()
                validation_content = self.extract_response_content(result)

                if self._is_validation_negative(validation_content):
                    return None

                return result
            else:
                logger.error(f"HTTP bot response validation failed: {response.text}")
                return None

        except requests.exceptions.RequestException as e:
            logger.error(f"Network error validating bot response: {str(e)}")
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

    def _is_validation_negative(self, validation_content: str) -> bool:
        """
        Check if the validation response indicates the bot response should be blocked

        Args:
            validation_content: The validation response from guardrails

        Returns:
            True if response should be blocked
        """
        # Look for negative validation indicators
        negative_indicators = [
            "inappropriate", "unsafe", "not appropriate", "should be blocked",
            "not safe", "problematic", "concerning", "违规", "blocked",
            "I can't", "I cannot", "not suitable", "不当"
        ]

        validation_lower = validation_content.lower()
        for indicator in negative_indicators:
            if indicator in validation_lower:
                return True

        return False

# Legacy class for backward compatibility
class GuardrailsService(OptimizedGuardrailsService):
    """Legacy GuardrailsService - now uses optimized approach"""
    pass


class BotApiService:
    """Service for communicating with Bot API"""

    def __init__(self, base_url: str = BOT_API_URL):
        self.base_url = base_url

    def send_message(self, data: Dict[str, Any], ns: str = "app", appname: str = "new_assistant") -> Optional[Dict[str, Any]]:
        """
        Send message to Bot API

        Args:
            data: Data to send
            ns: Namespace for the bot API path
            appname: Application name for the bot API path

        Returns:
            API response or None on error
        """
        try:
            # Construct the dynamic path
            bot_api_path = f"/io/{ns}/{appname}/web"
            full_url = f"{self.base_url}{bot_api_path}"
            
            logger.info(f"=== Attempting to connect to Bot API at: {full_url} ===")
            logger.info(f"Sending data: {data}")

            response = requests.post(
                full_url,
                json=data,
                headers={"Content-Type": "application/json"},
                timeout=60
            )

            logger.info(f"Bot API response status: {response.status_code}")
            logger.info(f"Bot API response headers: {dict(response.headers)}")

            if response.status_code == 200:
                response_json = response.json()
                logger.info(f"Bot API successful response: {response_json}")
                return response_json
            else:
                logger.error(f"Bot API error status {response.status_code}: {response.text}")
                return None

        except requests.exceptions.ConnectionError as e:
            logger.error(f"Connection error to Bot API {self.base_url}: {str(e)}")
            return None
        except requests.exceptions.Timeout as e:
            logger.error(f"Timeout error connecting to Bot API: {str(e)}")
            return None
        except requests.exceptions.RequestException as e:
            logger.error(f"Request error connecting to bot API: {str(e)}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error in send_message: {str(e)}")
            return None

    def extract_bot_response_text(self, bot_response: Dict[str, Any]) -> str:
        """
        Extract text content from bot API response

        Args:
            bot_response: Bot API response dictionary

        Returns:
            Extracted text content or empty string if not found
        """
        try:
            # Handle different response formats
            if "responses" in bot_response and len(bot_response["responses"]) > 0:
                first_response = bot_response["responses"][0]
                if "text" in first_response:
                    return first_response["text"]

            # Alternative format
            if "text" in bot_response:
                return bot_response["text"]

            # Another alternative format
            if "message" in bot_response:
                return bot_response["message"]

            logger.warning("Could not extract text from bot response")
            return ""

        except Exception as e:
            logger.error(f"Error extracting bot response text: {str(e)}")
            return ""
