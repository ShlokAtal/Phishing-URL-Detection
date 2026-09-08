import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split


PROJECT_ROOT = Path(__file__).resolve().parent.parent
CLEAN_DATASET_PATH = (
    PROJECT_ROOT / "dataset" / "processed" / "clean_url_features.csv"
)
TRAIN_DATASET_PATH = (
    PROJECT_ROOT / "dataset" / "processed" / "final_train.csv"
)
TEST_DATASET_PATH = (
    PROJECT_ROOT / "dataset" / "processed" / "final_test.csv"
)


df = pd.read_csv(CLEAN_DATASET_PATH)
X = df.drop("label", axis=1)
y = df["label"]
X_train, X_test, y_train, y_test = train_test_split(
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
print("FINAL TRAIN TEST SPLIT")
print("=" * 60)

print("\nTotal rows:", len(df))

print("Training rows:", len(train_df))
print("Testing rows:", len(test_df))

print("\nTraining label distribution:")
print(train_df["label"].value_counts())

print("\nTesting label distribution:")
print(test_df["label"].value_counts())

print("\nTraining dataset:")
print(TRAIN_DATASET_PATH)

print("\nTesting dataset:")
print(TEST_DATASET_PATH)

print("\n" + "=" * 60)
print("FINAL SPLIT COMPLETED")
print("=" * 60)