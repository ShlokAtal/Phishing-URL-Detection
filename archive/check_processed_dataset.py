import pandas as pd
from pathlib import Path

PROJECT_ROOT=Path(__file__).resolve().parent.parent
PROCESSED_DATASET_PATH=(
    PROJECT_ROOT / "dataset" / "processed" / "url_features.csv"
)

df=pd.read_csv(PROCESSED_DATASET_PATH)

print("="*60)
print("PROCESSED_DATASET_PATH")
print("="*60)

print("\n1. DATASET SIZE")
print("-"*60)
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\n2. COLUMN NAMES")
print("-" * 60)

for number, column in enumerate(df.columns, start=1):
    print(f"{number}. {column}")

print("\n3. MISSING VALUES")
print("-" * 60)
print(df.isnull().sum())

print("\n4. DUPLICATE ROWS")
print("-" * 60)
print("Duplicate rows:", df.duplicated().sum())

print("\n5. LABEL DISTRIBUTION")
print("-" * 60)
print(df["label"].value_counts())

print("\n6. DATA TYPES")
print("-" * 60)
print(df.dtypes)

print("\n" + "=" * 60)
print("VERIFICATION COMPLETED")
print("=" * 60)