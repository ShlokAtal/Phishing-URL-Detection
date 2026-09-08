import pandas as pd
import joblib
from pathlib import Path
from feature_extraction import extract_url_features
from risk_analyzer import analyze_risk

PROJECT_ROOT=Path(__file__).resolve().parent.parent
MODEL_PATH=PROJECT_ROOT/"models"/"random_forest_final.pkl"
FEATURE_ORDER=["URLLength","DomainLength","IsDomainIP","TLDLength","NoOfSubDomain","HasObfuscation","NoOfObfuscatedChar","ObfuscationRatio","NoOfLettersInURL","LetterRatioInURL","NoOfDegitsInURL","DegitRatioInURL","NoOfEqualsInURL","NoOfQMarkInURL","NoOfAmpersandInURL","NoOfOtherSpecialCharsInURL","SpacialCharRatioInURL","IsHTTPS"]

def predict_url(url):
    model=joblib.load(MODEL_PATH)
    features=extract_url_features(url)
    model_features={feature:features[feature] for feature in FEATURE_ORDER}
    
    features_df=pd.DataFrame([model_features],columns=FEATURE_ORDER)
    prediction=model.predict(features_df)[0]
    probabilities=model.predict_proba(features_df)[0]
    
    phishing_index=list(model.classes_).index(0)
    legitimate_index=list(model.classes_).index(1)
    phishing_probability=float(probabilities[phishing_index]*100)
    
    legitimate_probability=float(probabilities[legitimate_index]*100)
    rule_score,rule_level,reasons=analyze_risk(url,features)
    
    if rule_score>=60:
        final_prediction="Phishing"
        final_level="High"
        final_score=round(max(phishing_probability,rule_score),2)
        
    elif rule_score>=30:
        final_prediction="Suspicious"
        final_level="Medium"
        final_score=round(max((phishing_probability*0.4)+(rule_score*0.6),rule_score),2)
        
    else:
        final_prediction="Legitimate"
        final_level="Low"
        final_score=round(rule_score,2)
        
    if not reasons:
        reasons=["No major suspicious URL characteristics detected"]
    return {"url":url,"prediction":final_prediction,"risk_score":final_score,"risk_level":final_level,"model_probability":round(phishing_probability,2),"legitimate_probability":round(legitimate_probability,2),"reasons":reasons,"features":features}

if __name__=="__main__":
    url=input("Enter URL: ").strip()
    
    if not url:
        print("Error: Please enter a URL.")
    else:
        try:
            result=predict_url(url)
            print("\nPrediction:",result["prediction"])
            print("Risk Score:",f"{result['risk_score']:.2f}%")
            print("Risk Level:",result["risk_level"])
            
            print("Model Probability:",f"{result['model_probability']:.2f}%")
            print("Legitimate Probability:",f"{result['legitimate_probability']:.2f}%")
            print("\nReasons:")
            
            for reason in result["reasons"]:
                print("-",reason)
            print("\nFeatures:")
            
            for feature in FEATURE_ORDER:
                print(f"{feature}: {result['features'][feature]}")
        except Exception as error:
            print("\nPrediction error:",error)