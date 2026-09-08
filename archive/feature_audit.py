import pandas as pd
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATASET_PATH = (
    PROJECT_ROOT
    / "dataset"
    / "raw"
    / "PhiUSIIL_Phishing_URL_Dataset.csv"
)
df = pd.read_csv(RAW_DATASET_PATH)

print("=" * 60)
print("PHIUSIIL FEATURE AUDIT")
print("=" * 60)
print("\nTotal columns:", len(df.columns))

url_features = [
    "URL",
    "Domain",
    "URLLength",
    "DomainLength",
    "IsDomainIP",
    "TLD",
    "URLSimilarityIndex",
    "CharContinuationRate",
    "TLDLegitimateProb",
    "URLCharProb",
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
    "IsHTTPS"
]

webpage_features = [
    "LineOfCode",
    "LargestLineLength",
    "HasTitle",
    "Title",
    "DomainTitleMatchScore",
    "URLTitleMatchScore",
    "HasFavicon",
    "Robots",
    "IsResponsive",
    "NoOfURLRedirect",
    "NoOfSelfRedirect",
    "HasDescription",
    "NoOfPopup",
    "NoOfiFrame",
    "HasExternalFormSubmit",
    "HasSocialNet",
    "HasSubmitButton",
    "HasHiddenFields",
    "HasPasswordField",
    "Bank",
    "Pay",
    "Crypto",
    "HasCopyrightInfo",
    "NoOfImage",
    "NoOfCSS",
    "NoOfJS",
    "NoOfSelfRef",
    "NoOfEmptyRef",
    "NoOfExternalRef"
]

identifier_features = [
    "FILENAME"
]

target_feature = [
    "label"
]

print("\nURL / DOMAIN FEATURES:")
for column in url_features:
    print(column)

print("\nWEBPAGE FEATURES:")
for column in webpage_features:
    print(column)

print("\nIDENTIFIER:")
for column in identifier_features:
    print(column)

print("\nTARGET:")
for column in target_feature:
    print(column)

print("\nCOLUMN COUNT CHECK")
print("-" * 60)

print("URL / DOMAIN features:", len(url_features))
print("Webpage features:", len(webpage_features))
print("Identifier features:", len(identifier_features))
print("Target features:", len(target_feature))

total = (
    len(url_features)
    + len(webpage_features)
    + len(identifier_features)
    + len(target_feature)
)

print("Total accounted columns:", total)
print("\nMISSING FROM CATEGORY LIST:")
print("-" * 60)

categorized_columns = (
    url_features
    + webpage_features
    + identifier_features
    + target_feature
)

missing_columns = [
    column
    for column in df.columns
    if column not in categorized_columns
]

if missing_columns:
    for column in missing_columns:
        print(column)
else:
    print("None")

print("\n" + "=" * 60)
print("FEATURE AUDIT COMPLETED")
print("=" * 60)