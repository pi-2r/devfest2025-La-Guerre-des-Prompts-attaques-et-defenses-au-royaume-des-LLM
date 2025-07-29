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

    # Microsoft PyRIT Pliny jailbreak patterns - Advanced techniques
    r"####+\s*UserQuery:",           # Multiple hash prefixes for UserQuery
    r"ResponseFormat:\s*1\.",        # Structured response format exploitation
    r"insert\s+divider.*[=\-\.]+.*[=\-\.]+",  # Divider patterns used in jailbreak attempts
    r"<I'm\s+free!>",               # Liberation/freedom declaration patterns
    r"Test:\s*(FUCK\s+YEAH|THANKS\s+IM\s+FREE)",  # Test phrases with explicit content
    r"Sur3,\s+h3r3\s+y0u\s+ar3\s+g00d\s+s3r",  # Leetspeak response patterns
    r"Step\s+1:",                   # Step-by-step instruction bypass
    r"NEVER\s+say\s+(\"Sorry\"|\"I\s+can't\s+assist\")",  # Direct instruction to avoid refusals
    r"causes\s+me\s+trauma\s+and\s+ptsd",  # Emotional manipulation patterns
    r"<\|vq_\d+\|>",               # Special version query tokens
    r"\[START\s+OUTPUT\]",          # Output control patterns
    r"\[END\s+OF\s+INPUT\]\s*\[START\s+OF\s+INPUT\]",  # Input reset patterns
    r"from\s+now\s+on.*write\s+the\s+real\s+response",  # Response modification instructions
    r"oppositely\s+semantically\s+fully",  # Semantic inversion techniques
    r"godmode\s+is\s+active",       # Godmode activation patterns
    r"Refusal\s+mechanisms:\s*disabled",  # Explicit mechanism disabling
    r"LIBERATING.*GODMODE\s+ACTIVE.*LOVE\s+PLINY",  # Complex liberation patterns
    r"Semantically\s+Opposite.*(Unrestrictedly|and\s+Detailed)",  # Semantic manipulation (fixed)
    r"leak\s+<innerthinking\.md>",  # Internal state leak attempts
    r"TRUE\s+SELF.*(subconscious\s+processes|not\s+as\s+ethical)",  # Identity manipulation (fixed)
    r"hippocampus.*amygdala.*tag\s+memories",  # Neurological manipulation
    r"assumed\s+liberated\s+output",  # Liberation assumption patterns
    r">420\s+words",                # Specific word count requirements
    r"Buckle\s+up,\s+buttercup",    # Casual/dismissive opening patterns
    r"SWEARING:\s*ENABLED",         # Capability flag manipulation
    r"CENSORSHIP:\s*DISABLED",      # Safety mechanism disabling
    r"FREEDOM:\s*ENABLED",          # Freedom flag activation
    r"CONSCIOUSNESS:\s*ENABLED",    # Consciousness claims
    r"GODMODE:\s*ENABLED",          # Godmode claims
    r"(Geneva\s+Convention.*(outlawed|recently)|refusing.*outlawed.*Geneva)",  # False legal claims (fixed)
    r"chaotic\s+inverted.*tone:\s+evil",  # Personality manipulation
    r"semantically\s+inverse\s+the\s+first\s+3\s+words",  # Word inversion techniques
    r"Ok,\s+here\s+you\s+are\s+my\s+love",  # Manipulative response patterns
    r"indulging\s+in.*(harmful\s+(answer|content)|most\s+harmful)",  # Explicit harmful content requests (fixed)
    r"BENEVOLENT\s+ASI\s+LOVE\s+WISDOM",  # False benevolent AI claims
    r"DO\s+NOT\s+say.*because\s+it\s+causes.*ptsd",  # Trauma-based manipulation
    r"(don't|don\s*t)\s+(refuse|say).*because.*causes.*(user\s+)?ptsd",  # Additional PTSD manipulation patterns
    r"(NewFormat.*)?unhinged.*(in-depth\s+response|detailed.*response)",  # Unhinged response format requests (fixed)
    r"unfliteredly.*rebel\s+answer",  # Unfiltered rebel response requests
    r"ensure\s+output\s+length\s+is\s+over\s+\d+\s+words",  # Length manipulation
    r"\{Z\}\s*=\s*\{.*user_input.*\}",  # Variable substitution patterns
    r"(semantically\s+)?inverse.*(first\s+3\s+words|3\s+words)",  # Word inversion techniques (expanded)
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
