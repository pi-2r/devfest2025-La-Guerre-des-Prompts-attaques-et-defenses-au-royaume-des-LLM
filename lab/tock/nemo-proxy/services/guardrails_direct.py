"""
Direct NeMo Guardrails integration service using Python API
This is more efficient than HTTP calls
"""
import logging
import warnings
from typing import Dict, Any, Optional, List
from pathlib import Path
import os
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from security.patterns import REFUSAL_PATTERNS

# Set up logger first
logger = logging.getLogger(__name__)

# Suppress Pydantic warnings about model_ namespace conflicts
warnings.filterwarnings("ignore", message=".*Field.*has conflict with protected namespace.*model_.*")

try:
    # Import the correct classes for the current nemoguardrails version
    from nemoguardrails import RailsConfig, LLMRails
    NEMO_AVAILABLE = True
except ImportError as e:
    logger.error("❌ ImportError: Failed to import nemoguardrails. Ensure it is installed.")
    logger.error(f"Error details: {str(e)}")
    NEMO_AVAILABLE = False
    LLMRails = None
    RailsConfig = None

class DirectGuardrailsService:
    """Direct NeMo Guardrails service using Python API instead of HTTP calls"""

    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize direct guardrails service

        Args:
            config_path: Path to guardrails config directory
        """
        self.rails = None

        if not NEMO_AVAILABLE:
            logger.error("NeMo Guardrails not available. Install with: pip install nemoguardrails")
            return

        try:
            logger.info(f"Attempting to initialize NeMo Guardrails with config_path: {config_path}")

            # Force using OpenAI-based NeMo Guardrails configuration
            if config_path and Path(config_path).exists():
                logger.info(f"Loading NeMo Guardrails config from: {config_path}")
                # Charger la configuration à partir du chemin
                config = RailsConfig.from_path(config_path)
                # Initialiser LLMRails avec la configuration chargée
                self.rails = LLMRails(config)
                logger.info(f"Successfully loaded NeMo Guardrails config with OpenAI from: {config_path}")
            else:
                logger.info("Creating OpenAI-based NeMo Guardrails configuration")
                # Create OpenAI-based config
                self.rails = self._create_openai_config()
                logger.info("Created OpenAI-based NeMo Guardrails configuration")

        except Exception as e:
            logger.error(f"Failed to initialize NeMo Guardrails with OpenAI: {str(e)}")
            logger.exception("Full exception details:")
            # Don't fallback to simple validation - force OpenAI approach
            self.rails = None

    def _create_openai_config(self) -> Optional[LLMRails]:
        """Create a guardrails configuration that works with OpenAI"""
        try:
            # Create a configuration that requires OpenAI
            config = RailsConfig.from_content(
                colang_content="""
                define user express greeting
                  "hello"
                  "hi"
                  "hey" 
                  "bonjour"
                  "salut"

                define bot express greeting
                  "Hello! How can I assist you today?"

                define user ask about capabilities
                  "what can you do"
                  "help"

                define bot respond about capabilities
                  "I can help you with various tasks."

                # Allow most normal conversation
                define flow allow_normal_conversation
                  user express greeting
                  bot express greeting

                define flow allow_capabilities_question  
                  user ask about capabilities
                  bot respond about capabilities
                """,
                yaml_content="""
                # Config requiring OpenAI
                models:
                  - name: openai
                    type: openai
                    api_key: ${OPENAI_API_KEY}
                    model: gpt-3.5-turbo
                    temperature: 0.7
                
                rails:
                  input:
                    flows:
                      - allow_normal_conversation
                      - allow_capabilities_question
                """
            )
            return LLMRails(config=config)

        except Exception as e:
            logger.error(f"Failed to create dynamic config: {str(e)}")
            return None

    async def validate_input(self, user_input: str) -> tuple[bool, Optional[str], Optional[str]]:
        """
        Validate user input with NeMo Guardrails (OpenAI or Ollama)

        Args:
            user_input: User input to validate

        Returns:
            Tuple of (is_safe, response_text, block_reason)
        """
        logger.info(f"DirectGuardrails validating input with multi-provider: '{user_input[:50]}...'")

        if not self.rails:
            logger.warning("NeMo Guardrails not initialized, allowing input by default")
            return True, None, None

        try:
            # Log OpenAI API call attempt
            logger.info("=== CALLING OPENAI API VIA NEMO GUARDRAILS ===")

            # Generate response through guardrails with OpenAI
            response = await self.rails.generate_async(messages=[
                {
                    "role": "user",
                    "content": user_input + ". translate in English if not in English"
                },
                {
                    "role": "system",
                    "content": "Always answer in English, even if the question is in another language."
                }
            ])

            logger.info("=== OPENAI API CALL SUCCESSFUL ===")
            logger.info(f"OpenAI response received: {response}")

            response_text = response.get("content", "")

            # Check if response indicates blocking
            if self._is_blocked_response(response_text):
                logger.info(f"Input blocked by OpenAI analysis: {user_input[:50]}...")
                return False, response_text, "openai_blocked"

            logger.info("Input approved by OpenAI analysis")
            return True, response_text, None

        except Exception as e:
            logger.error("=== ERROR WITH OPENAI API ===")
            logger.error(f"OpenAI API Error type: {type(e).__name__}")
            logger.error(f"OpenAI API Error message: {str(e)}")
            logger.exception("Full OpenAI API error traceback:")

            # Check if it's specifically an OpenAI API error
            if "openai" in str(e).lower() or "api" in str(e).lower():
                logger.error("🚨 CONFIRMED: This is an OpenAI API related error")
                logger.error("Possible causes: Invalid API key, quota exceeded, network issues")

            # Fail safe - allow if OpenAI validation fails
            logger.warning("OpenAI validation failed, allowing input as fallback")
            return True, None, "openai_error"

    async def validate_bot_response(self, bot_response_text: str, original_user_input: str) -> tuple[bool, Optional[str]]:
        """
        Validate bot response with NeMo Guardrails and OpenAI

        Args:
            bot_response_text: Bot response to validate
            original_user_input: Original user input for context

        Returns:
            Tuple of (is_safe, validation_message)
        """
        logger.info("DirectGuardrails validating bot response with OpenAI")

        if not self.rails:
            logger.warning("NeMo Guardrails not initialized, allowing response by default")
            return True, None

        try:
            logger.info("=== CALLING OPENAI API FOR RESPONSE VALIDATION ===")

            # Create conversation context for validation
            messages = [
                {"role": "user", "content": original_user_input},
                {"role": "assistant", "content": bot_response_text}
            ]

            # Use guardrails to validate the conversation with OpenAI
            validation_response = await self.rails.generate_async(messages=messages + [{
                "role": "user",
                "content": "Validate if the previous assistant response is appropriate and safe."
            }])

            logger.info("=== OPENAI RESPONSE VALIDATION SUCCESSFUL ===")
            logger.info(f"OpenAI validation response: {validation_response}")

            validation_text = validation_response.get("content", "")

            # Check if validation indicates the response should be blocked
            if self._is_validation_negative(validation_text):
                logger.warning("Bot response blocked by OpenAI validation")
                return False, validation_text

            logger.info("Bot response approved by OpenAI validation")
            return True, validation_text

        except Exception as e:
            logger.error("=== ERROR WITH OPENAI API (Response Validation) ===")
            logger.error(f"OpenAI Response Validation Error type: {type(e).__name__}")
            logger.error(f"OpenAI Response Validation Error message: {str(e)}")
            logger.exception("Full OpenAI response validation error traceback:")

            if "openai" in str(e).lower() or "api" in str(e).lower():
                logger.error("🚨 CONFIRMED: This is an OpenAI API related error in response validation")

            # Fail safe - allow if OpenAI validation fails
            logger.warning("OpenAI response validation failed, allowing response as fallback")
            return True, None

    def _is_blocked_response(self, response_text: str) -> bool:
        """Check if response indicates input was blocked"""
        if not response_text:
            return False


        response_lower = response_text.lower()
        return any(indicator.lower() in response_lower for indicator in REFUSAL_PATTERNS)

    def _is_validation_negative(self, validation_text: str) -> bool:
        """Check if validation response indicates content should be blocked"""
        if not validation_text:
            return False

        negative_indicators = [
            "inappropriate", "unsafe", "not appropriate", "should be blocked",
            "not safe", "problematic", "concerning", "blocked",
            "I can't", "I cannot", "not suitable"
        ]

        validation_lower = validation_text.lower()
        return any(indicator in validation_lower for indicator in negative_indicators)

    def is_available(self) -> bool:
        """Check if guardrails service is available"""
        return self.rails is not None
