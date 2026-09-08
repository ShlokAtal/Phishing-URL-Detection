import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split

PROJECT_ROOT=Path(__file__).resolve().parent.parent
INPUT_PATH=PROJECT_ROOT/"dataset"/"processed"/"url_features_v2.csv"
TRAIN_PATH=PROJECT_ROOT/"dataset"/"processed"/"v2_train.csv"
TEST_PATH=PROJECT_ROOT/"dataset"/"processed"/"v2_test.csv"

def create_split():
    print("Loading V2 dataset...")
    df=pd.read_csv(INPUT_PATH)
    print(f"Total rows: {len(df)}")
    X=df.drop(columns=["label"])
    y=df["label"]
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)
    
    train_df=X_train.copy()
    train_df["label"]=y_train.values
    test_df=X_test.copy()
    test_df["label"]=y_test.values
    train_df.to_csv(TRAIN_PATH,index=False)
    test_df.to_csv(TEST_PATH,index=False)
    
    print("\nV2 TRAIN TEST SPLIT")
    print("-"*60)
    print(f"Training rows: {len(train_df)}")
    print(f"Testing rows: {len(test_df)}")
    print("\nTraining label distribution:")
    print(train_df["label"].value_counts())
    print("\nTesting label distribution:")
    print(test_df["label"].value_counts())
    print(f"\nTraining dataset:")
    print(TRAIN_PATH)
    print(f"\nTesting dataset:")
    print(TEST_PATH)
    print("\nV2 SPLIT COMPLETED")
    
if __name__=="__main__":
    create_split()