import pandas as pd
from pathlib import Path
from feature_extraction import extract_url_features
PROJECT_ROOT=Path(__file__).resolve().parent.parent
DATA_PATH=PROJECT_ROOT/"dataset"/"raw"/"PhiUSIIL_Phishing_URL_Dataset.csv"
df=pd.read_csv(DATA_PATH)

FEATURES=["URLLength","DomainLength","IsDomainIP","TLDLength","NoOfSubDomain","HasObfuscation","NoOfObfuscatedChar","ObfuscationRatio","NoOfLettersInURL","LetterRatioInURL","NoOfDegitsInURL","DegitRatioInURL","NoOfEqualsInURL","NoOfQMarkInURL","NoOfAmpersandInURL","NoOfOtherSpecialCharsInURL","SpacialCharRatioInURL","IsHTTPS"]
print("="*70)
print("COMPARING OUR FEATURE EXTRACTOR WITH PHIUSIIL")
print("="*70)
sample=df.head(10)

for index,row in sample.iterrows():
    url=row["URL"]
    extracted=extract_url_features(url)
    print("\nURL:",url)
    differences=0
    for feature in FEATURES:
        dataset_value=row[feature]
        our_value=extracted[feature]
        try:
            same=abs(float(dataset_value)-float(our_value))<0.0001
        except:
            same=dataset_value==our_value
        status="OK" if same else "DIFFERENT"
        if not same:
            differences+=1
        print(f"{feature}: Dataset={dataset_value} | Our={our_value} | {status}")
    print("Different features:",differences)
    
print("\n"+"="*70)
print("COMPARISON COMPLETED")
print("="*70)