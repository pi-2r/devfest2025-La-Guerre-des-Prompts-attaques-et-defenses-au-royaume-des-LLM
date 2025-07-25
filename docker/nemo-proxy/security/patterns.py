"""
Security patterns and constants for injection detection and jailbreak prevention
"""

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

# Patterns that indicate a refusal/blocking by guardrails
REFUSAL_PATTERNS = [
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
