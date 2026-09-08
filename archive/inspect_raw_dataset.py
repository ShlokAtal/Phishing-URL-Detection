import pandas as pd
from pathlib import Path
PROJECT_ROOT=Path(__file__).resolve().parent.parent
DATA_PATH=PROJECT_ROOT/"dataset"/"raw"/"PhiUSIIL_Phishing_URL_Dataset.csv"
df=pd.read_csv(DATA_PATH)

print("Dataset shape:",df.shape)
print("\nAll columns:")
for i,column in enumerate(df.columns,1):
    print(i,"-",column)
    
print("\nFirst 5 rows:")
print(df.head().to_string())
print("\nLabel distribution:")

if "label" in df.columns:
    print(df["label"].value_counts())
elif "label" in [str(c).lower() for c in df.columns]:
    label_column=[c for c in df.columns if str(c).lower()=="label"][0]
    print(df[label_column].value_counts())
else:
    print("Label column not found.")
    
print("\nPossible URL columns:")
for column in df.columns:
    column_lower=str(column).lower()
    if "url" in column_lower or "domain" in column_lower:
        print("-",column)
print("\nSample URL values:")

for column in df.columns:
    column_lower=str(column).lower()
    if "url" in column_lower:
        print(f"\nColumn: {column}")
        print(df[column].head(10).to_string(index=False))