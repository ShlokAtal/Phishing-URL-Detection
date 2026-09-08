import pandas as pd
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
TRAIN_DATASET_PATH = (
    PROJECT_ROOT / "dataset" / "processed" / "train.csv"
)
TEST_DATASET_PATH = (
    PROJECT_ROOT / "dataset" / "processed" / "test.csv"
)
train_df = pd.read_csv(TRAIN_DATASET_PATH)
test_df = pd.read_csv(TEST_DATASET_PATH)

feature_columns = [
    column for column in train_df.columns
    if column != "label"
]
train_features = set(
    train_df[feature_columns].itertuples(index=False, name=None)
)
test_features = set(
    test_df[feature_columns].itertuples(index=False, name=None)
)
overlap = train_features.intersection(test_features)

print("=" * 60)
print("TRAIN / TEST FEATURE OVERLAP ANALYSIS")
print("=" * 60)
print("\nTraining rows:", len(train_df))
print("Testing rows:", len(test_df))
print("\nUnique training feature combinations:", len(train_features))
print("Unique testing feature combinations:", len(test_features))
print("\nFeature combinations appearing in both sets:", len(overlap))
print(
    "\nPercentage of test feature combinations also in training:"
)
print(f"{(len(overlap) / len(test_features)) * 100:.2f}%")

print("\n" + "=" * 60)
print("ANALYSIS COMPLETED")
print("=" * 60)