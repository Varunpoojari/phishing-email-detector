import re
from typing import Dict, List

class PhishingDetector:
    def __init__(self):
        # Common phishing keywords and patterns
        self.suspicious_patterns = [
            r'urgent',
            r'account.*suspend',
            r'verify.*account',
            r'banking.*detail',
            r'credit.*card',
            r'click.*link',
            r'limited.*time',
            r'password.*expired'
        ]
        
        # Initialize risk score thresholds
        self.LOW_RISK = 0.3
        self.MEDIUM_RISK = 0.6
        self.HIGH_RISK = 0.8

    def analyze_email(self, email_content: str, email_metadata: Dict) -> Dict:
        """Analyzes email content and metadata for potential phishing attempts."""
        content = email_content.lower()
        matches = []
        risk_score = 0.0
        
        for pattern in self.suspicious_patterns:
            if re.search(pattern, content):
                matches.append(pattern)
                risk_score += 0.2
        
        risk_score = min(risk_score, 1.0)
        
        if risk_score >= self.HIGH_RISK:
            risk_level = "High"
        elif risk_score >= self.MEDIUM_RISK:
            risk_level = "Medium"
        elif risk_score >= self.LOW_RISK:
            risk_level = "Low"
        else:
            risk_level = "Safe"
        
        return {
            "risk_score": risk_score,
            "risk_level": risk_level,
            "suspicious_patterns_found": matches
        }

def main():
    detector = PhishingDetector()
    
    sample_email = """
    URGENT: Your account will be suspended!
    
    Dear valued customer,
    
    We detected suspicious activity on your account. Please verify your banking details
    immediately by clicking the link below. This is a limited time warning.
    
    Best regards,
    Security Team
    """
    
    sample_metadata = {
        "sender": "security@bank-example.com",
        "subject": "URGENT: Account Suspension Notice",
        "date": "2024-02-02"
    }
    
    results = detector.analyze_email(sample_email, sample_metadata)
    
    print("\nPhishing Detection Results:")
    print(f"Risk Level: {results['risk_level']}")
    print(f"Risk Score: {results['risk_score']:.2f}")
    print("Suspicious Patterns Found:", ", ".join(results['suspicious_patterns_found']))

if __name__ == "__main__":
    main()