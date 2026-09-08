import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split


PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROCESSED_DATASET_PATH = (
    PROJECT_ROOT / "dataset" / "processed" / "url_features.csv"
)
TRAIN_DATASET_PATH = (
    PROJECT_ROOT / "dataset" / "processed" / "train.csv"
)
TEST_DATASET_PATH = (
    PROJECT_ROOT / "dataset" / "processed" / "test.csv"
)
df = pd.read_csv(PROCESSED_DATASET_PATH)

X=df.drop("label", axis=1)
y=df["label"]

X_train, X_test, y_train, y_test=train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

train_df = X_train.copy()
train_df["label"] = y_train.values

test_df = X_test.copy()
test_df["label"] = y_test.values

train_df.to_csv(TRAIN_DATASET_PATH, index=False)
test_df.to_csv(TEST_DATASET_PATH, index=False)

print("=" * 60)
print("TRAIN TEST SPLIT")
print("=" * 60)

print("\nTotal rows:", len(df))

print("\nTraining rows:", len(train_df))
print("Testing rows:", len(test_df))

print("\nTraining label distribution:")
print(train_df["label"].value_counts())

print("\nTesting label distribution:")
print(test_df["label"].value_counts())

print("\nTraining dataset saved to:")
print(TRAIN_DATASET_PATH)

print("\nTesting dataset saved to:")
print(TEST_DATASET_PATH)

print("\n" + "=" * 60)
print("TRAIN TEST SPLIT COMPLETED")
print("=" * 60)