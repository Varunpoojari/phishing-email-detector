# AI-Powered Phishing Email Detector

A Python-based tool that uses Natural Language Processing techniques to detect potential phishing attempts in emails.

## Features

- Analyzes email content and metadata for suspicious patterns
- Provides risk scoring and classification
- Easy to use and extend

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Varunpoojari/phishing-email-detector.git
cd phishing-email-detector
```

2. Run the detector:
```bash
python3 phishing_detector.py
```

## Usage

```python
from phishing_detector import PhishingDetector

detector = PhishingDetector()
results = detector.analyze_email(email_content, email_metadata)
print(results)
```

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
