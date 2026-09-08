import pandas as pd 
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATASET_DIR = PROJECT_ROOT / "dataset" / "raw"
csv_files = list(RAW_DATASET_DIR.glob("*.csv"))

if not csv_files:
    print("ERROR: No CSV file found in dataset/raw/")
    exit()
if len(csv_files)>1:
    print("Multiple CSV files found:")
    for file in csv_files:
        print(f"- {file.name}")
    print("\n Please keep only the PhiUSIIL dataset CSV in dataset/raw/ for now.")
    exit()

dataset_path=csv_files[0]

print("="*60)
print("PHISHING URL DATASET EXPLORATION")
print("="*60)
print(f"\n Dataset file:{dataset_path.name}")

df=pd.read_csv(dataset_path)

print("\n1. DATASET SIZE")
print("-"*60)
print(f"Number of rows:{df.shape[0]}")
print(f"Number of columns:{df.shape[1]}")

print("\n2. COLUMN NAMES")
print("-"*60)
for i, column in enumerate(df.columns, start=1):
    print(f"{i}. {column}")
    
print("\n3. FIRST 5 RECORDS")
print("-" * 60)
print(df.head())

print("\n4. DATA TYPES")
print("-" * 60)
print(df.dtypes)

print("\n5. MISSING VALUES")
print("-" * 60)
missing_values = df.isnull().sum()
print(missing_values)

print("\n6. DUPLICATE RECORDS")
print("-" * 60)
duplicate_count = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicate_count}")

print("\n7. BASIC STATISTICS")
print("-" * 60)
print(df.describe(include="all").transpose())

print("\n8. POSSIBLE LABEL COLUMNS")
print("-" * 60)

print("\n"+"="*60)
print("DATASET EXPLORATION COMPLETED")
print("="*60)

print("\n9. LABEL DISTRIBUTION")
print("-"*60)
print(df["label"].value_counts())

for column in df.columns:
    unique_values = df[column].dropna().unique()
    if len(unique_values) <= 10:
        print(f"\nColumn: {column}")
        print(f"Unique values: {unique_values}")

print("\n" + "=" * 60)
print("DATASET EXPLORATION COMPLETED")
print("=" * 60)