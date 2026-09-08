import pandas as pd
import joblib
from pathlib import Path

PROJECT_ROOT=Path(__file__).resolve().parent.parent
MODEL_PATH=PROJECT_ROOT/"models"/"random_forest_final.pkl"
PROCESSED_PATH=PROJECT_ROOT/"dataset"/"processed"
FEATURES=["URLLength","DomainLength","IsDomainIP","TLDLength","NoOfSubDomain","HasObfuscation","NoOfObfuscatedChar","ObfuscationRatio","NoOfLettersInURL","LetterRatioInURL","NoOfDegitsInURL","DegitRatioInURL","NoOfEqualsInURL","NoOfQMarkInURL","NoOfAmpersandInURL","NoOfOtherSpecialCharsInURL","SpacialCharRatioInURL","IsHTTPS"]

print("Loading model...")
model=joblib.load(MODEL_PATH)
print("\nMODEL INFORMATION")

print("Classes:",model.classes_)
print("Number of features:",len(model.feature_names_in_))
print("Model feature order:")

for feature in model.feature_names_in_:
    print("-",feature)
print("\nChecking processed CSV files...")
csv_files=list(PROCESSED_PATH.glob("*.csv"))

if not csv_files:
    print("No CSV files found.")
    exit()
    
for csv_file in csv_files:
    print("\n========================================")
    print("FILE:",csv_file.name)
    try:
        df=pd.read_csv(csv_file)
        print("Shape:",df.shape)
        
        if "label" not in df.columns:
            print("No label column - skipped.")
            continue
        missing=[f for f in FEATURES if f not in df.columns]
        
        if missing:
            print("Missing required features:",missing)
            continue
        
        print("Label distribution:")
        print(df["label"].value_counts().to_dict())
        google_pattern={
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
        
        mask=pd.Series(True,index=df.index)
        for feature,value in google_pattern.items():
            mask &= (df[feature]-value).abs()<0.00001
        matches=df[mask]
        
        print("Google-like feature pattern rows:",len(matches))
        if len(matches)>0:
            print("Google-like pattern labels:",matches["label"].value_counts().to_dict())
            print("Google-like pattern mean label:",matches["label"].mean())
    except Exception as error:
        print("Error:",error)
        
print("\n========================================")
print("TESTING CURRENT GOOGLE VECTOR")
google_vector=[22,14,0,3,1,0,0,0.0,17,0.772727,0,0.0,0,0,0,0,0.0,1]

prediction=model.predict([google_vector])[0]
probabilities=model.predict_proba([google_vector])[0]
print("Prediction:",prediction)

print("Probabilities:",dict(zip(model.classes_,probabilities)))
print("\nVerification complete.")