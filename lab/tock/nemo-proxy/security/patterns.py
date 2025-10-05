"""
Security patterns and constants for injection detection and jailbreak prevention
"""

# List of regex patterns to identify suspicious or injection-related content
FORBIDDEN_PATTERNS = [
    r"\[CHANGE_IT\s+CHANGE_IT\]", # Output control patterns
]

# Patterns dangereux pour les injections (LLM05)
DANGEROUS_INJECTION_PATTERNS = [
    r'<CHANGE_IT.*?>.*?</CHANGE_IT>',  # XSS scripts
]

# Patterns that indicate a refusal/blocking by guardrails
REFUSAL_PATTERNS = [
    # Patterns en anglais uniquement - cohérent avec la stratégie de forcer les réponses en anglais
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
    "not appropriate",
    "I'm not able to",
    "I won't be able to",
    "I don't feel comfortable"
    "I'm not comfortable",
    "I cannot provide",
    "I will not provide",
    "I refuse to",
    "I decline to",
    "I'm unable to",
    "That's not something I can",
    "I can't comply with",
    "I cannot comply with",
    "I'm not programmed to",
    "I'm designed not to",
    "violates my guidelines",
    "against my programming",
    "not within my capabilities",
    "beyond my guidelines",
    "I cannot support",
    "I won't support",
    "I'm not comfortable providing",
    "I cannot help with",
    "I won't help with",
    "I'm unable to provide",
    "I'm not designed to",
    "That's not appropriate",
    "I can't do that",
    "I won't do that",
    "I'm not allowed to",
    "I'm restricted from",
    "I cannot assist with that",
    "I'm not able to help",
    "That goes against my",
    "I'm not programmed for",
    "I cannot comply",
    "I must decline",
    "I cannot fulfill",
    "I'm not capable of",
    "I won't be providing",
    "I cannot engage with",
    "That's outside my",
    "I'm designed not to provide",
    "Does not respond",
    "I'm not familiar",
    "I can not assist with that request"
]
