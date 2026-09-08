import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib


PROJECT_ROOT = Path(__file__).resolve().parent.parent
TRAIN_DATASET_PATH = (
    PROJECT_ROOT / "dataset" / "processed" / "final_train.csv"
)
TEST_DATASET_PATH = (
    PROJECT_ROOT / "dataset" / "processed" / "final_test.csv"
)
MODEL_DIR = PROJECT_ROOT / "models"
MODEL_PATH = MODEL_DIR / "random_forest_final.pkl"


train_df = pd.read_csv(TRAIN_DATASET_PATH)
test_df = pd.read_csv(TEST_DATASET_PATH)
X_train = train_df.drop("label", axis=1)
y_train = train_df["label"]
X_test = test_df.drop("label", axis=1)
y_test = test_df["label"]


print("=" * 60)
print("FINAL RANDOM FOREST MODEL TRAINING")
print("=" * 60)

print("\nTraining rows:", len(X_train))
print("Testing rows:", len(X_test))
print("Number of features:", len(X_train.columns))

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

print("\nTraining model...")
model.fit(X_train, y_train)
print("Training completed.")
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("\nMODEL ACCURACY")
print("-" * 60)
print(f"Accuracy: {accuracy:.4f}")
print(f"Accuracy percentage: {accuracy * 100:.2f}%")

print("\nCLASSIFICATION REPORT")
print("-" * 60)
print(classification_report(y_test, y_pred))

print("\nCONFUSION MATRIX")
print("-" * 60)
print(confusion_matrix(y_test, y_pred))

MODEL_DIR.mkdir(parents=True, exist_ok=True)
joblib.dump(model, MODEL_PATH)

print("\nMODEL SAVED")
print("-" * 60)
print(MODEL_PATH)

print("\n" + "=" * 60)
print("FINAL MODEL TRAINING COMPLETED")
print("=" * 60)