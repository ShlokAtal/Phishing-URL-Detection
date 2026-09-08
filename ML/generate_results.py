import pandas as pd
import joblib
from pathlib import Path
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

PROJECT_ROOT=Path(__file__).resolve().parent.parent
MODEL_PATH=PROJECT_ROOT/"models"/"random_forest_final.pkl"
TRAIN_PATH=PROJECT_ROOT/"dataset"/"processed"/"final_train.csv"
TEST_PATH=PROJECT_ROOT/"dataset"/"processed"/"final_test.csv"
RESULTS_PATH=PROJECT_ROOT/"Results"
FEATURES=["URLLength","DomainLength","IsDomainIP","TLDLength","NoOfSubDomain","HasObfuscation","NoOfObfuscatedChar","ObfuscationRatio","NoOfLettersInURL","LetterRatioInURL","NoOfDegitsInURL","DegitRatioInURL","NoOfEqualsInURL","NoOfQMarkInURL","NoOfAmpersandInURL","NoOfOtherSpecialCharsInURL","SpacialCharRatioInURL","IsHTTPS"]
RESULTS_PATH.mkdir(exist_ok=True)

print("Loading model and datasets...")
model=joblib.load(MODEL_PATH)
train_df=pd.read_csv(TRAIN_PATH)

test_df=pd.read_csv(TEST_PATH)
X_test=test_df[FEATURES]
y_test=test_df["label"]

predictions=model.predict(X_test)
accuracy=accuracy_score(y_test,predictions)
report=classification_report(y_test,predictions,labels=[0,1],target_names=["Phishing","Legitimate"])

cm=confusion_matrix(y_test,predictions,labels=[0,1])
print(f"Test Accuracy: {accuracy*100:.2f}%")
print("\nClassification Report:")
print(report)

print("\nConfusion Matrix:")
print(cm)
result_text=f"""PHISHGUARD - MACHINE LEARNING RESULTS
========================================
Model: Random Forest Classifier
Training Dataset: final_train.csv
Testing Dataset: final_test.csv
Number of Training Samples: {len(train_df)}
Number of Testing Samples: {len(test_df)}
Number of Features: {len(FEATURES)}
Label Meaning:
0 = Phishing
1 = Legitimate
TEST ACCURACY
------------
{accuracy*100:.2f}%
CLASSIFICATION REPORT
---------------------
{report}
CONFUSION MATRIX
----------------
Rows = Actual
Columns = Predicted
             Phishing  Legitimate
Phishing     {cm[0][0]:9d}  {cm[0][1]:10d}
Legitimate   {cm[1][0]:9d}  {cm[1][1]:10d}
FEATURE IMPORTANCE
------------------
"""
importance=pd.DataFrame({"Feature":FEATURES,"Importance":model.feature_importances_}).sort_values("Importance",ascending=False)
for _,row in importance.iterrows():
    result_text+=f"{row['Feature']}: {row['Importance']:.6f}\n"
result_text+="""\nNOTE
----
The deployed PhishGuard application combines the Random Forest model output
with rule-based risk analysis for the final risk classification.
"""
with open(RESULTS_PATH/"model_results.txt","w",encoding="utf-8") as file:
    file.write(result_text)
    
plt.figure(figsize=(7,6))
plt.imshow(cm)
plt.title("PhishGuard - Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("Actual Label")
plt.xticks([0,1],["Phishing","Legitimate"])
plt.yticks([0,1],["Phishing","Legitimate"])

for i in range(2):
    for j in range(2):
        plt.text(j,i,str(cm[i,j]),ha="center",va="center")
plt.tight_layout()
plt.savefig(RESULTS_PATH/"confusion_matrix.png",dpi=300)
plt.close()
plt.figure(figsize=(10,7))
plt.barh(importance["Feature"],importance["Importance"])

plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("PhishGuard - Feature Importance")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(RESULTS_PATH/"feature_importance.png",dpi=300)
plt.close()

print("\nResults generated successfully!")
print(f"Saved to: {RESULTS_PATH}")