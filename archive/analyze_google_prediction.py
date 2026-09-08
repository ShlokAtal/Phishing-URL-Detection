import pandas as pd
import joblib
from pathlib import Path

PROJECT_ROOT=Path(__file__).resolve().parent.parent
MODEL_PATH=PROJECT_ROOT/"models"/"random_forest_final.pkl"
model=joblib.load(MODEL_PATH)

FEATURES=list(model.feature_names_in_)
google={
"URLLength":22,
"DomainLength":14,
"IsDomainIP":0,
"TLDLength":3,
"NoOfSubDomain":1,
"HasObfuscation":0,
"NoOfObfuscatedChar":0,
"ObfuscationRatio":0.0,
"NoOfLettersInURL":17,
"LetterRatioInURL":0.772727,
"NoOfDegitsInURL":0,
"DegitRatioInURL":0.0,
"NoOfEqualsInURL":0,
"NoOfQMarkInURL":0,
"NoOfAmpersandInURL":0,
"NoOfOtherSpecialCharsInURL":0,
"SpacialCharRatioInURL":0.0,
"IsHTTPS":1
}

X=pd.DataFrame([google],columns=FEATURES)
prediction=model.predict(X)[0]
probability=model.predict_proba(X)[0]

print("BASELINE GOOGLE PREDICTION")
print("Prediction:",prediction)
print("Phishing probability:",probability[list(model.classes_).index(0)])
print("Legitimate probability:",probability[list(model.classes_).index(1)])
print("\nFEATURE VALUES")

for feature in FEATURES:
    print(f"{feature}: {google[feature]}")
    
print("\nFEATURE IMPORTANCE")
importance=pd.Series(model.feature_importances_,index=FEATURES).sort_values(ascending=False)
print(importance.to_string())
print("\nTESTING FEATURE CHANGES")

for feature in FEATURES:
    modified=google.copy()
    if modified[feature] in [0,1]:
        modified[feature]=1-modified[feature]
    elif modified[feature]>0:
        modified[feature]=modified[feature]*2
    else:
        modified[feature]=1
    test_X=pd.DataFrame([modified],columns=FEATURES)
    
    test_probability=model.predict_proba(test_X)[0]
    phishing_probability=test_probability[list(model.classes_).index(0)]
    print(f"{feature}: {phishing_probability*100:.2f}% phishing")