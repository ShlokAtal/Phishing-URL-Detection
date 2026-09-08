import pandas as pd
from pathlib import Path

PROJECT_ROOT=Path(__file__).resolve().parent.parent
DATA_PATH=PROJECT_ROOT/"dataset"/"processed"/"url_features.csv"
df=pd.read_csv(DATA_PATH)

print("Dataset shape:",df.shape)
print("\nActual dataset columns:")

for i,column in enumerate(df.columns,1):
    print(i,"-",column)
print("\nLabel distribution:")
print(df["label"].value_counts())

COLUMN_MAP={
    "URLLength":["URLLength","URLLenght"],
    "DomainLength":["DomainLength","DomainLenght"],
    "IsDomainIP":["IsDomainIP"],
    "TLDLength":["TLDLength","TLDLenght"],
    "NoOfSubDomain":["NoOfSubDomain","HasOfSubDomain"],
    "HasObfuscation":["HasObfuscation"],
    "NoOfObfuscatedChar":["NoOfObfuscatedChar"],
    "ObfuscationRatio":["ObfuscationRatio"],
    "NoOfLettersInURL":["NoOfLettersInURL"],
    "LetterRatioInURL":["LetterRatioInURL"],
    "NoOfDegitsInURL":["NoOfDegitsInURL"],
    "DegitRatioInURL":["DegitRatioInURL"],
    "NoOfEqualsInURL":["NoOfEqualsInURL"],
    "NoOfQMarkInURL":["NoOfQMarkInURL"],
    "NoOfAmpersandInURL":["NoOfAmpersandInURL"],
    "NoOfOtherSpecialCharsInURL":["NoOfOtherSpecialCharsInURL"],
    "SpacialCharRatioInURL":["SpacialCharRatioInURL"],
    "IsHTTPS":["IsHTTPS"]
}

FEATURES=[]
for standard_name,possible_names in COLUMN_MAP.items():
    found_name=None
    for name in possible_names:
        if name in df.columns:
            found_name=name
            break
    if found_name:
        FEATURES.append(found_name)
    else:
        print(f"\nWARNING: Feature not found: {standard_name}")
        
print("\nFeatures used for analysis:")
for feature in FEATURES:
    print("-",feature)
    
print("\nMean feature values by label:")
print(df.groupby("label")[FEATURES].mean().round(4).to_string())
print("\nHTTPS distribution by label:")

print(pd.crosstab(df["IsHTTPS"],df["label"],normalize="index").round(4))
print("\nCommon structural patterns:")
pattern=df.groupby(FEATURES)["label"].agg(["count","mean"])
print(pattern.sort_values("count",ascending=False).head(20).to_string())