import pandas as pd
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATASET_PATH = (
    PROJECT_ROOT
    / "dataset"
    / "raw"
    / "PhiUSIIL_Phishing_URL_Dataset.csv"
)

CLEAN_DATASET_PATH=(
    PROJECT_ROOT / "dataset" / "processed" /  "clean_url_features.csv" 
)

df=pd.read_csv(RAW_DATASET_PATH)
df=df.drop_duplicates(subset=["URL"])

feature_columns = [
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
    "label"
]

clean_df=df[feature_columns]
clean_df.to_csv(CLEAN_DATASET_PATH, index=False)

print("="*60)
print("CLEAN DATASET CREATION")
print("="*60)

print("\nOriginal rows:",235795)
print("Rows after removing duplicate URLs:",len(df))
print("\nColumns:",len(clean_df.columns))

print("\nLabel distribution:")
print(clean_df["label"].value_counts())

print("\nSaved to:")
print(CLEAN_DATASET_PATH)

print("\n" + "=" * 60)
print("CLEAN DATASET CREATED")
print("=" * 60)