import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from predict import predict_url

urls=[
    "https://www.google.com",
    "https://www.wikipedia.org",
    "http://paypal-login-security-example.invalid",
    "http://192.168.1.100/login"
]

for url in urls:
    print("="*60)
    print(f"URL: {url}")
    print("="*60)
    try:
        result=predict_url(url)
        print(f"Prediction: {result['prediction']}")
        print(f"Risk Score: {result['risk_score']}%")
        print(f"Risk Level: {result['risk_level']}")
        print(f"Model Probability: {result['model_probability']}%")
        print("Reasons:")
        for reason in result.get("reasons",[]):
            print(f"- {reason}")
    except Exception as error:
        print(f"ERROR: {error}")