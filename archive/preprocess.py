import pandas as pd
from pathlib import Path
from feature_extraction import extract_url_features
PROJECT_ROOT=Path(__file__).resolve().parent.parent
RAW_DATASET_PATH=PROJECT_ROOT/"dataset"/"raw"/"PhiUSIIL_Phishing_URL_Dataset.csv"
PROCESSED_DATASET_PATH=PROJECT_ROOT/"dataset"/"processed"/"url_features_v2.csv"
def create_processed_dataset():
    print("Loading dataset...")
    df=pd.read_csv(RAW_DATASET_PATH)
    print(f"Total rows: {len(df)}")
    processed_rows=[]
    for index,row in df.iterrows():
        try:
            features=extract_url_features(str(row["URL"]))
            features["label"]=int(row["label"])
            processed_rows.append(features)
        except Exception:
            continue
        if (index+1)%10000==0:
            print(f"Processed: {index+1}/{len(df)}")
    processed_df=pd.DataFrame(processed_rows)
    PROCESSED_DATASET_PATH.parent.mkdir(parents=True,exist_ok=True)
    processed_df.to_csv(PROCESSED_DATASET_PATH,index=False)
    print(f"Processed dataset saved to: {PROCESSED_DATASET_PATH}")
    print(f"Processed rows: {len(processed_df)}")
    print(f"Processed columns: {len(processed_df.columns)}")
    print("\nColumns:")
    for column in processed_df.columns:
        print(column)
if __name__=="__main__":
    create_processed_dataset()