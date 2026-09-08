import pandas as pd
import joblib
from pathlib import Path

PROJECT_ROOT=Path(__file__).resolve().parent.parent
MODEL_PATH=PROJECT_ROOT/"models"/"random_forest_v2.pkl"
TRAIN_PATH=PROJECT_ROOT/"dataset"/"processed"/"v2_train.csv"

model=joblib.load(MODEL_PATH)
train_df=pd.read_csv(TRAIN_PATH)
features=train_df.drop(columns=["label"]).columns
importance=model.feature_importances_
result=pd.DataFrame({"Feature":features,"Importance":importance})
result=result.sort_values("Importance",ascending=False)

print("="*60)
print("V2 FEATURE IMPORTANCE")
print("="*60)
print()
for _,row in result.iterrows():
    print(f"{row['Feature']:<30} {row['Importance']:.6f}")
print()
print("="*60)
print("FEATURE IMPORTANCE ANALYSIS COMPLETED")
print("="*60)