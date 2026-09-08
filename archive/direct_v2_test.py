import pandas as pd
import joblib
from pathlib import Path
from feature_extraction import extract_url_features

PROJECT_ROOT=Path(__file__).resolve().parent.parent
MODEL_PATH=PROJECT_ROOT/"models"/"random_forest_v2.pkl"

FEATURE_ORDER=[
    "URLLength",
    "DomainLength",
    "IsDomainIP",
    "TLDLength",
    "NoOfSubDomain",
    "HasObfuscation",
    "NoOfObfuscatedChar",
    "ObfuscationRatio",
    "NoOfLettersInURL",
    "LetterRatioInURL",
    "NoOfDegitsInURL",
    "DegitRatioInURL",
    "NoOfEqualsInURL",
    "NoOfQMarkInURL",
    "NoOfAmpersandInURL",
    "NoOfOtherSpecialCharsInURL",
    "SpacialCharRatioInURL",
    "IsHTTPS",
    "HasSuspiciousWord",
    "NoOfSuspiciousWords",
    "HasBrandName",
    "NoOfHyphens",
    "NoOfDots",
    "PathLength",
    "HasLoginKeyword",
    "HasVerifyKeyword",
    "HasAccountKeyword"
]

model=joblib.load(MODEL_PATH)

urls=[
    "https://www.google.com",
    "https://www.wikipedia.org",
    "http://paypal-login-security-example.invalid",
    "http://192.168.1.100/login"
]

for url in urls:
    print("="*70)
    print(f"URL: {url}")
    print("="*70)
    features=extract_url_features(url)
    features_df=pd.DataFrame([[features[column] for column in FEATURE_ORDER]],columns=FEATURE_ORDER)
    prediction=model.predict(features_df)[0]
    probabilities=model.predict_proba(features_df)[0]
    print(f"Prediction: {'Phishing' if prediction==1 else 'Legitimate'}")
    print(f"Legitimate probability: {probabilities[0]*100:.2f}%")
    print(f"Phishing probability: {probabilities[1]*100:.2f}%")
    print("\nNew feature values:")
    print(f"HasSuspiciousWord: {features['HasSuspiciousWord']}")
    print(f"NoOfSuspiciousWords: {features['NoOfSuspiciousWords']}")
    print(f"HasBrandName: {features['HasBrandName']}")
    print(f"NoOfHyphens: {features['NoOfHyphens']}")
    print(f"NoOfDots: {features['NoOfDots']}")
    print(f"PathLength: {features['PathLength']}")
    print(f"HasLoginKeyword: {features['HasLoginKeyword']}")
    print(f"HasVerifyKeyword: {features['HasVerifyKeyword']}")
    print(f"HasAccountKeyword: {features['HasAccountKeyword']}")