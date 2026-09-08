
from feature_extraction import extract_url_features
from risk_analyzer import analyze_risk
urls=["https://www.google.com","https://www.wikipedia.org","http://paypal-login-security-example.invalid","http://192.168.1.100/login"]
for url in urls:
    features=extract_url_features(url)
    score,level,reasons=analyze_risk(url,features)
    print("="*60)
    print(f"URL: {url}")
    print(f"Risk Score: {score}%")
    print(f"Risk Level: {level}")
    print("Reasons:")
    for reason in reasons:
        print(f"- {reason}")