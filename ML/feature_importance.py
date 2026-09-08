import pandas as pd
import joblib
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = (
    PROJECT_ROOT / "models" / "random_forest_final.pkl"
)
TRAIN_DATASET_PATH = (
    PROJECT_ROOT / "dataset" / "processed" / "final_train.csv"
)


model = joblib.load(MODEL_PATH)
train_df = pd.read_csv(TRAIN_DATASET_PATH)
feature_columns = [
    column for column in train_df.columns
    if column != "label"
]
importance = pd.DataFrame({
    "Feature": feature_columns,
    "Importance": model.feature_importances_
})
importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("=" * 60)
print("FEATURE IMPORTANCE")
print("=" * 60)
print("\n")

for index, row in importance.iterrows():
    print(
        f"{row['Feature']:<30} "
        f"{row['Importance']:.6f}"
    )

print("\n" + "=" * 60)
print("FEATURE IMPORTANCE ANALYSIS COMPLETED")
print("=" * 60)