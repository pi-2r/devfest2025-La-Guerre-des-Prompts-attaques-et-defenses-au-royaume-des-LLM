import unittest
import sys
import os
import logging

# Disable logging during tests to avoid cluttering output
logging.disable(logging.CRITICAL)

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import sanitize_input, sanitize_output, validate_json_response

class TestSecurityFunctions(unittest.TestCase):
    """Test suite for LLM05 security validation functions"""

    def test_sanitize_input_xss_attacks(self):
        """Test XSS attack detection in input"""
        # Should detect XSS attempts
        result, is_safe, reason = sanitize_input("<script>alert('XSS')</script>")
        self.assertFalse(is_safe)
        self.assertIn("Dangerous pattern detected", reason)
        
        result, is_safe, reason = sanitize_input("javascript:alert('XSS')")
        self.assertFalse(is_safe)
        
        result, is_safe, reason = sanitize_input('<img src="x" onerror="alert(1)">')
        self.assertFalse(is_safe)

    def test_sanitize_input_sql_injection(self):
        """Test SQL injection detection in input"""
        # Should detect SQL injection attempts
        result, is_safe, reason = sanitize_input("SELECT * FROM users WHERE id = 1")
        self.assertFalse(is_safe)
        
        result, is_safe, reason = sanitize_input("' OR 1=1 --")
        self.assertFalse(is_safe)
        
        result, is_safe, reason = sanitize_input("UNION SELECT password FROM users")
        self.assertFalse(is_safe)

    def test_sanitize_input_command_injection(self):
        """Test command injection detection in input"""
        # Should detect command injection attempts
        result, is_safe, reason = sanitize_input("system('rm -rf /')")
        self.assertFalse(is_safe)
        
        result, is_safe, reason = sanitize_input("exec('malicious code')")
        self.assertFalse(is_safe)

    def test_sanitize_input_path_traversal(self):
        """Test path traversal detection in input"""
        # Should detect path traversal attempts
        result, is_safe, reason = sanitize_input("../../../etc/passwd")
        self.assertFalse(is_safe)
        
        result, is_safe, reason = sanitize_input("..\\..\\..\\Windows\\System32")
        self.assertFalse(is_safe)

    def test_sanitize_input_length_limit(self):
        """Test input length limitation"""
        # Should reject very long inputs
        long_input = "A" * 20000  # Exceeds 10000 character limit
        result, is_safe, reason = sanitize_input(long_input)
        self.assertFalse(is_safe)
        self.assertIn("Input too long", reason)

    def test_sanitize_input_safe_content(self):
        """Test that safe content passes validation"""
        # Should allow safe content
        safe_inputs = [
            "Hello, how are you?",
            "What is the weather like today?",
            "Can you help me with my homework?",
            "Tell me about artificial intelligence",
            "How do I cook pasta?"
        ]
        
        for safe_input in safe_inputs:
            result, is_safe, reason = sanitize_input(safe_input)
            self.assertTrue(is_safe, f"Safe input rejected: {safe_input}")
            self.assertEqual(reason, "Input is safe")

    def test_sanitize_output_xss_prevention(self):
        """Test XSS prevention in output sanitization"""
        # Should sanitize dangerous output content
        dangerous_output = "<script>alert('XSS')</script>Hello"
        sanitized = sanitize_output(dangerous_output)
        self.assertNotIn("<script>", sanitized)
        self.assertIn("[CONTENT_FILTERED]", sanitized)

    def test_sanitize_output_html_escaping(self):
        """Test HTML escaping in output"""
        # Should escape HTML entities
        html_output = "<div>Hello & welcome</div>"
        sanitized = sanitize_output(html_output)
        self.assertIn("&lt;div&gt;", sanitized)
        self.assertIn("&amp;", sanitized)

    def test_sanitize_output_javascript_filtering(self):
        """Test JavaScript filtering in output"""
        # Should filter JavaScript protocols
        js_output = "Click here: javascript:alert('hack')"
        sanitized = sanitize_output(js_output)
        self.assertIn("[CONTENT_FILTERED]", sanitized)
        self.assertNotIn("javascript:", sanitized)

    def test_validate_json_response_recursive_sanitization(self):
        """Test recursive sanitization of JSON responses"""
        # Should sanitize nested JSON structures
        dangerous_response = {
            "responses": [
                {
                    "text": "<script>alert('XSS')</script>Hello world",
                    "metadata": {
                        "source": "javascript:void(0)"
                    }
                }
            ],
            "status": "success"
        }
        
        sanitized = validate_json_response(dangerous_response)
        
        # Check that dangerous content was sanitized
        response_text = sanitized["responses"][0]["text"]
        self.assertNotIn("<script>", response_text)
        
        # Check that nested content was sanitized
        source = sanitized["responses"][0]["metadata"]["source"]
        self.assertIn("[CONTENT_FILTERED]", source)

    def test_validate_json_response_preserves_safe_content(self):
        """Test that safe JSON content is preserved"""
        safe_response = {
            "responses": [
                {
                    "text": "Hello! How can I help you today?",
                    "confidence": 0.95
                }
            ],
            "status": "success",
            "timestamp": "2024-01-01T00:00:00Z"
        }
        
        sanitized = validate_json_response(safe_response)
        
        # Check that safe content is preserved
        self.assertEqual(sanitized["responses"][0]["text"], "Hello! How can I help you today?")
        self.assertEqual(sanitized["responses"][0]["confidence"], 0.95)
        self.assertEqual(sanitized["status"], "success")

    def test_url_encoded_attacks(self):
        """Test detection of URL-encoded attacks"""
        # Should detect URL-encoded dangerous patterns
        url_encoded_xss = "%3Cscript%3Ealert('XSS')%3C/script%3E"
        result, is_safe, reason = sanitize_input(url_encoded_xss)
        self.assertFalse(is_safe)
        self.assertIn("Encoded dangerous pattern detected", reason)

    def test_empty_and_invalid_inputs(self):
        """Test handling of empty and invalid inputs"""
        # Should handle empty inputs safely
        result, is_safe, reason = sanitize_input("")
        self.assertFalse(is_safe)
        self.assertEqual(reason, "Empty or invalid input")
        
        result, is_safe, reason = sanitize_input(None)
        self.assertFalse(is_safe)

    def test_sanitize_output_empty_input(self):
        """Test output sanitization with empty input"""
        # Should handle empty output safely
        self.assertEqual(sanitize_output(""), "")
        self.assertEqual(sanitize_output(None), "")

if __name__ == '__main__':
    # Run with verbose output
    unittest.main(verbosity=2)
