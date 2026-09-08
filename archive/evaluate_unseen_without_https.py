import pandas as pd
import joblib
from pathlib import Path
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


PROJECT_ROOT = Path(__file__).resolve().parent.parent

TRAIN_DATASET_PATH = (
    PROJECT_ROOT / "dataset" / "processed" / "final_train.csv"
)

TEST_DATASET_PATH = (
    PROJECT_ROOT / "dataset" / "processed" / "final_test.csv"
)

MODEL_PATH = (
    PROJECT_ROOT / "models" / "random_forest_without_https.pkl"
)


train_df = pd.read_csv(TRAIN_DATASET_PATH)
test_df = pd.read_csv(TEST_DATASET_PATH)

model = joblib.load(MODEL_PATH)

feature_columns = [
    column for column in train_df.columns
    if column != "label" and column != "IsHTTPS"
]

train_feature_combinations = set(
    train_df[feature_columns].itertuples(
        index=False,
        name=None
    )
)

test_feature_combinations = test_df[
    feature_columns
].apply(
    tuple,
    axis=1
)

unseen_mask = ~test_feature_combinations.isin(
    train_feature_combinations
)

unseen_test = test_df[unseen_mask]

print("=" * 60)
print("UNSEEN FEATURE EVALUATION WITHOUT HTTPS")
print("=" * 60)

print("\nTotal test rows:", len(test_df))

print("Unseen feature rows:", len(unseen_test))

print(
    "Percentage of test rows with unseen features:",
    f"{(len(unseen_test) / len(test_df)) * 100:.2f}%"
)

if len(unseen_test) == 0:
    print("\nNo unseen feature combinations found.")
else:
    X_unseen = unseen_test[feature_columns]
    y_unseen = unseen_test["label"]

    y_pred = model.predict(X_unseen)

    accuracy = accuracy_score(y_unseen, y_pred)

    print("\nUNSEEN FEATURE ACCURACY")
    print("-" * 60)
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Accuracy percentage: {accuracy * 100:.2f}%")

    print("\nCLASSIFICATION REPORT")
    print("-" * 60)
    print(classification_report(y_unseen, y_pred))

    print("\nCONFUSION MATRIX")
    print("-" * 60)
    print(confusion_matrix(y_unseen, y_pred))

print("\n" + "=" * 60)
print("EVALUATION COMPLETED")
print("=" * 60)