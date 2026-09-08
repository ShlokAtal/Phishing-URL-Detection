import pandas as pd
import joblib
from pathlib import Path
PROJECT_ROOT=Path(__file__).resolve().parent.parent
MODEL_PATH=PROJECT_ROOT/"models"/"random_forest_final.pkl"
TRAIN_PATH=PROJECT_ROOT/"dataset"/"processed"/"train.csv"
TEST_PATH=PROJECT_ROOT/"dataset"/"processed"/"test.csv"
FEATURE_ORDER=["URLLength","DomainLength","IsDomainIP","TLDLength","NoOfSubDomain","HasObfuscation","NoOfObfuscatedChar","ObfuscationRatio","NoOfLettersInURL","LetterRatioInURL","NoOfDegitsInURL","DegitRatioInURL","NoOfEqualsInURL","NoOfQMarkInURL","NoOfAmpersandInURL","NoOfOtherSpecialCharsInURL","SpacialCharRatioInURL","IsHTTPS"]
model=joblib.load(MODEL_PATH)

print("Model classes:",model.classes_)
print("Number of features:",len(model.feature_names_in_))

print("Model features:")
for feature in model.feature_names_in_:
    print("-",feature)
print("\nTesting common URL feature patterns...")

test_urls={
    "Google":[22,14,0,3,1,0,0,0.0,17,0.772727,0,0.0,0,0,0,0,0.227273,1],
    "Wikipedia":[25,17,0,3,1,0,0,0.0,20,0.8,0,0.0,0,0,0,0,0.2,1],
    "Microsoft":[25,17,0,3,1,0,0,0.0,20,0.8,0,0.0,0,0,0,0,0.2,1],
    "Amazon":[22,14,0,3,1,0,0,0.0,17,0.772727,0,0.0,0,0,0,0,0.227273,1],
    "GitHub":[22,14,0,3,1,0,0,0.0,17,0.772727,0,0.0,0,0,0,0,0.227273,1]
}

for name,values in test_urls.items():
    df=pd.DataFrame([values],columns=FEATURE_ORDER)
    prediction=model.predict(df)[0]
    probabilities=model.predict_proba(df)[0]
    
    print(f"\n{name}")
    print("Prediction:",prediction)
    print("Class probabilities:",dict(zip(model.classes_,probabilities)))