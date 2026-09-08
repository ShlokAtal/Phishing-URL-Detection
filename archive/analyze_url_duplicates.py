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
print("RAW URL DUPLICATE ANALYSIS")
print("=" * 60)

print("\nTotal rows:", len(df))
print("\nUnique URLs:", df["URL"].nunique())
print("\nDuplicate URL rows:", df["URL"].duplicated().sum())

url_label_counts = (
    df.groupby("URL")["label"]
    .nunique()
)
conflicting_urls = (
    url_label_counts[url_label_counts > 1]
)

print("\nURLs with conflicting labels:", len(conflicting_urls))
print("\nLabel distribution:")
print(df["label"].value_counts())

print("\n" + "=" * 60)
print("ANALYSIS COMPLETED")
print("=" * 60)