import pandas as pd
import joblib
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

PROJECT_ROOT=Path(__file__).resolve().parent.parent
TRAIN_PATH=PROJECT_ROOT/"dataset"/"processed"/"v2_train.csv"
TEST_PATH=PROJECT_ROOT/"dataset"/"processed"/"v2_test.csv"
MODEL_PATH=PROJECT_ROOT/"models"/"random_forest_v2.pkl"

def train_model():
    print("="*60)
    print("V2 RANDOM FOREST MODEL TRAINING")
    print("="*60)
    train_df=pd.read_csv(TRAIN_PATH)
    test_df=pd.read_csv(TEST_PATH)
    X_train=train_df.drop(columns=["label"])
    y_train=train_df["label"]
    X_test=test_df.drop(columns=["label"])
    y_test=test_df["label"]
    
    print(f"\nTraining rows: {len(X_train)}")
    print(f"Testing rows: {len(X_test)}")
    print(f"Number of features: {len(X_train.columns)}")
    print("\nFeatures:")
    
    for feature in X_train.columns:
        print(f"- {feature}")
    model=RandomForestClassifier(
        n_estimators=300,
        random_state=42,
        n_jobs=-1,
        class_weight="balanced"
    )
    
    print("\nTraining model...")
    model.fit(X_train,y_train)
    print("Training completed.")
    predictions=model.predict(X_test)
    accuracy=accuracy_score(y_test,predictions)
    
    print("\nMODEL ACCURACY")
    print("-"*60)
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Accuracy percentage: {accuracy*100:.2f}%")
    print("\nCLASSIFICATION REPORT")
    print("-"*60)
    print(classification_report(y_test,predictions))
    print("\nCONFUSION MATRIX")
    print("-"*60)
    print(confusion_matrix(y_test,predictions))
    
    MODEL_PATH.parent.mkdir(parents=True,exist_ok=True)
    joblib.dump(model,MODEL_PATH)
    
    print("\nMODEL SAVED")
    print("-"*60)
    print(MODEL_PATH)
    print("\n"+"="*60)
    print("V2 MODEL TRAINING COMPLETED")
    print("="*60)

if __name__=="__main__":
    train_model()