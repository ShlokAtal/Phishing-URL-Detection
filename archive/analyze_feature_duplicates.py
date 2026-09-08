import pandas as pd
from pathlib import Path

PROJECT_ROOT=Path(__file__).resolve().parent.parent
PROCESSED_DATASET_PATH=(
    PROJECT_ROOT / "dataset" / "processed" / "url_features.csv"
)

df=pd.read_csv(PROCESSED_DATASET_PATH)
feature_columns=[column for column in df.columns if column !="label"]

grouped=(
    df.groupby(feature_columns)["label"]
    .agg(["count","nunique"])
    .reset_index()
)
conflicting=grouped[grouped["nunique"]>1]

print("="*60)
print("DUPLICATED FEATURES ANALYSIS")
print("="*60)

print("\nTotal rows:",len(df))
print("Unique feature combinations:",len(grouped))
print("Unique feature combinations with conflicting labels:",len(conflicting))
print("\nTotal duplicate feature rows:",len(df)-len(grouped))

print("\nLabel distribution:")
print(df["label"].value_counts())

print("\n"+"="*60)
print("ANALYSIS COMPLETED")
print("="*60)