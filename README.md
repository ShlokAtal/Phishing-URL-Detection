# 🛡️ PhishGuard
## Phishing URL Detection Using Machine Learning in Cybersecurity

PhishGuard is a Machine Learning-based cybersecurity application designed to detect potentially malicious phishing URLs.

The system analyzes the structure and characteristics of a URL, extracts security-related features, uses a trained Random Forest Classifier to estimate whether the URL is phishing or legitimate, and combines the Machine Learning output with a rule-based risk analyzer to provide a final user-friendly result.

The application provides a web interface where users can enter a URL and receive:

- Phishing / Suspicious / Legitimate prediction
- Risk score
- Risk level
- Phishing probability
- Legitimate probability
- Reasons for detected suspicious characteristics
- Extracted URL features

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Problem Statement](#-problem-statement)
- [Objectives](#-objectives)
- [Project Scope](#-project-scope)
- [How the System Works](#️-how-the-system-works)
- [System Architecture](#-system-architecture)
- [Machine Learning Model](#-machine-learning-model)
- [Dataset](#-dataset)
- [Features Used / URL Characteristics Analyzed](#-url-characteristics-analyzed)
- [Project Structure](#-project-structure)
- [Complete Data Flow](#-complete-data-flow)
- [Security Considerations](#-security-considerations)
- [Limitations](#️-limitations)
- [Future Scope](#-future-scope)
- [Main Concepts Demonstrated](#-main-concepts-demonstrated)
- [Development Environment](#-development-environment)

---

## 🔎 About the Project

Phishing is one of the most common cybersecurity threats on the Internet.

In a phishing attack, an attacker creates a malicious website or URL that attempts to imitate a legitimate website. The victim may then be tricked into providing sensitive information such as:

- Username
- Password
- Banking information
- Credit/debit card information
- OTP
- Personal information
- Account credentials

Attackers may create suspicious URLs using characteristics such as:

- Very long URLs
- Multiple subdomains
- Large numbers of digits
- Excessive special characters
- IP addresses instead of domain names
- URL obfuscation
- Missing HTTPS
- Suspicious keywords
- Brand impersonation

PhishGuard attempts to identify these characteristics automatically.

Instead of manually inspecting a URL, the system converts the URL into numerical features and uses Machine Learning and rule-based security analysis to evaluate it.

---

## ❗ Problem Statement

Users frequently encounter suspicious links through:

- Email
- SMS
- Social media
- Messaging applications
- Advertisements
- Websites
- Online communication

It can be difficult for an ordinary user to determine whether a URL is safe.

The goal of this project is to develop a Machine Learning-based system that can analyze URL characteristics and assist users in identifying potentially phishing URLs.

---

## 🎯 Objectives

The main objectives of PhishGuard are:

1. Detect potentially phishing URLs using Machine Learning.
2. Extract useful security-related features from URLs.
3. Train a Random Forest classification model.
4. Evaluate the trained model using a held-out test dataset.
5. Provide a simple web-based interface for URL analysis.
6. Generate a risk score for the submitted URL.
7. Explain suspicious characteristics detected in the URL.
8. Demonstrate the practical use of Machine Learning in cybersecurity.

---

## 📋 Project Scope

The current version of PhishGuard focuses on **URL-based phishing detection**.

The system analyzes the URL itself rather than opening or crawling the target website.

### Included

- URL input
- URL preprocessing
- URL feature extraction
- Machine Learning classification
- Random Forest model
- Rule-based risk analysis
- Risk scoring
- Risk-level classification
- Explanation of suspicious characteristics
- FastAPI backend
- HTML/CSS/JavaScript frontend
- Model evaluation
- Feature importance analysis

### Not Included

The current version does not include:

- Website crawling
- Website HTML analysis
- Browser extension
- Live DNS analysis
- WHOIS lookup
- Live threat-intelligence APIs
- Automatic website blocking
- Credential protection
- Cloud deployment

These features can be considered for future development.

---

## ⚙️ How the System Works

The complete workflow is:

```text
                    ┌───────────────────┐
                    │    User enters    │
                    │        URL        │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │   URL Processing  │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Feature Extraction│
                    │    18 Features    │
                    └─────────┬─────────┘
                              │
                 ┌────────────┴────────────┐
                 │                         │
                 ▼                         ▼
       ┌───────────────────┐     ┌───────────────────┐
       │   Random Forest   │     │   Rule-Based Risk │
       │       Model       │     │      Analyzer     │
       └─────────┬─────────┘     └─────────┬─────────┘
                 │                         │
                 │                         ▼
                 │                ┌───────────────────┐
                 │                │  Risk Score +     │
                 │                │     Reasons       │
                 │                └─────────┬─────────┘
                 │                          │
                 └────────────┬─────────────┘
                              ▼
                    ┌───────────────────┐
                    │  Hybrid Decision  │
                    └─────────┬─────────┘
                              │
                              ▼
              ┌──────────────────────────────┐
              │        Final Result          │
              │                              │
              │  Phishing                    │
              │  Suspicious                  │
              │  Legitimate                  │
              │                              │
              │  Risk Score                  │
              │  Risk Level                  │
              │  Reasons                     │
              └──────────────────────────────┘
```

---

## 🏗️ System Architecture

```text
┌──────────────────────────────────────────┐
│                Frontend UI                │
│         HTML + CSS + JavaScript           │
└────────────────────┬───────────────────────┘
                      │ HTTP Request
                      ▼
┌──────────────────────────────────────────┐
│              FastAPI Backend              │
│                app/main.py                │
└────────────────────┬───────────────────────┘
                      │
                      ▼
┌──────────────────────────────────────────┐
│            Prediction Module              │
│                predict.py                 │
└───────────────┬────────────────────────────┘
                 │
         ┌───────┴────────┐
         ▼                ▼
┌────────────────┐  ┌─────────────────────┐
│    Feature      │  │   Rule-Based Risk   │
│   Extraction    │  │      Analyzer       │
│                 │  │                     │
│ feature_        │  │  risk_analyzer.py   │
│ extraction.py   │  │                     │
└────────┬────────┘  └──────────┬──────────┘
         │                      │
         ▼                      │
┌────────────────────┐          │
│   Random Forest     │          │
│       Model         │          │
│                      │          │
│ random_forest_       │          │
│ final.pkl             │          │
└──────────┬───────────┘          │
           │                      │
           └──────────┬───────────┘
                       ▼
              ┌───────────────────┐
              │  Final Prediction │
              │  + Risk Analysis  │
              └───────────────────┘
```

---

## 🤖 Machine Learning Model

The main Machine Learning algorithm used in this project is:

**Random Forest Classifier**

Random Forest is an ensemble Machine Learning algorithm based on multiple decision trees. Instead of depending on a single decision tree, Random Forest combines predictions from many trees to produce a final classification.

### Model Configuration

| Parameter        | Value |
|-------------------|-------|
| Algorithm         | Random Forest Classifier |
| Number of Trees   | 100 |
| Random State      | 42 |
| Parallel Jobs     | -1 |

The primary trained model is:

```
models/random_forest_final.pkl
```

The model is loaded using the `joblib` library during prediction.

---

## 📊 Dataset

The project uses the **PhiUSIIL Phishing URL Dataset**.

The PhiUSIIL dataset contains phishing and legitimate URL examples along with URL and webpage-related characteristics.

### Dataset Information Used in This Project

| Property   | Value |
|------------|-------|
| Instances  | 235,795 |
| Columns    | 56 |

### Dataset Labels

| Label | Meaning |
|-------|---------|
| 0     | Phishing |
| 1     | Legitimate |

The original dataset contains many features. For the deployed Machine Learning model, a selected set of **18 URL-oriented features** is used. These features can be extracted directly from a submitted URL without visiting the target website.

### Dataset Sources

- **UCI Machine Learning Repository** — https://archive.ics.uci.edu/dataset/967/phiusil-phishing-url-dataset
- **Mendeley Data** — https://data.mendeley.com/datasets/shwpxscxy2/2

---

## 🧩 URL Characteristics Analyzed

### Domain Characteristics
- Domain length
- IP address usage
- Number of subdomains
- TLD length

### Character Characteristics
- Number of letters
- Number of digits
- Special characters
- Character ratios

### URL Structure
- URL length
- Query marks
- Equals signs
- Ampersands
- URL path

### Security Characteristics
- HTTPS
- Obfuscated characters

---

## 📁 Project Structure

```text
Phishing-URL-Detection/
│
├── app/
│   ├── main.py
│   │
│   ├── static/
│   │   ├── script.js
│   │   └── style.css
│   │
│   └── templates/
│       └── index.html
│
├── ML/
│   ├── feature_extraction.py
│   ├── feature_importance.py
│   ├── generate_results.py
│   ├── predict.py
│   ├── risk_analyzer.py
│   └── train_final_model.py
│
├── models/
│   ├── random_forest_final.pkl
│   ├── random_forest_model.pkl
│   ├── random_forest_v2.pkl
│   └── random_forest_without_https.pkl
│
├── dataset/
│   ├── raw/
│   │   └── PhiUSIIL_Phishing_URL_Dataset.csv
│   │
│   └── processed/
│       ├── clean_url_features.csv
│       ├── final_train.csv
│       ├── final_test.csv
│       ├── test.csv
│       ├── train.csv
│       └── other processed datasets
│
├── Results/
│   ├── confusion_matrix.png
│   ├── feature_importance.png
│   └── model_results.txt
│
├── archive/
│   └── Previous development and experiment scripts
│
├── requirements.txt
└── test_setup.py
```

---

## 🔄 Complete Data Flow

```text
PhiUSIIL Dataset
       │
       ▼
Data Cleaning
       │
       ▼
Feature Selection
       │
       ▼
Train/Test Split
       │
       ▼
Random Forest Training
       │
       ▼
Model Evaluation
       │
       ▼
Saved Model
       │
       ▼
random_forest_final.pkl
       │
       ▼
User submits URL
       │
       ▼
Feature Extraction
       │
       ▼
18 Features
       │
       ├───────────────┐
       ▼               ▼
Random Forest     Rule-Based
Prediction        Risk Analysis
       │               │
       └───────┬───────┘
               ▼
       Hybrid Decision
               │
               ▼
      Final Application Result
```

---

## 🔐 Security Considerations

PhishGuard is primarily an educational and academic cybersecurity project.

The application analyzes the submitted URL without intentionally browsing the target website.

It does not:

- Enter credentials
- Download files from the target website
- Submit forms
- Interact with the target website
- Guarantee website safety
- Replace professional security products

---

## ⚠️ Limitations

1. **URL-Based Detection** — The system primarily analyzes URL characteristics. It does not inspect the complete webpage.
2. **No Live Threat Intelligence** — The application does not currently query live threat-intelligence databases.
3. **No Website Content Analysis** — HTML, JavaScript, images, forms, and webpage behavior are not analyzed.
4. **Dataset Dependency** — Machine Learning performance depends on the quality and distribution of the training dataset.
5. **False Positives and False Negatives** — No Machine Learning system is perfect. A legitimate URL may be classified incorrectly, and a phishing URL may sometimes evade detection.
6. **HTTPS Limitation** — HTTPS indicates encrypted communication but does not prove that a website is trustworthy.
7. **Evolving Attacks** — New phishing techniques may not be represented in the training dataset.

---

## 🚀 Future Scope

PhishGuard can be extended with additional cybersecurity capabilities.

### 🌐 Real-Time Threat Intelligence
Integrate threat-intelligence services to check URLs against known malicious URL databases.

### 🔎 Website Content Analysis
Analyze:
- HTML
- JavaScript
- Forms
- External resources
- Login pages
- Redirect behavior

### 🌍 Domain Analysis
Add:
- Domain age
- WHOIS information
- DNS information
- IP reputation
- SSL certificate information

### 🧠 Advanced Machine Learning
Experiment with:
- Gradient Boosting
- XGBoost
- LightGBM
- Neural Networks
- Deep Learning
- NLP-based URL analysis

### 🌐 Browser Extension
Develop a browser extension that automatically analyzes links while browsing.

### ☁️ Cloud Deployment
Deploy the application to a cloud platform so users can access it remotely.

### 🔄 Continuous Learning
Automatically retrain the model using newly collected phishing URLs.

### 📱 Mobile Application
Develop a mobile application for checking suspicious links.

---

## 📚 Main Concepts Demonstrated

```text
Python
   │
   ├── Data Processing
   │
   ├── Feature Engineering
   │
   └── Machine Learning
          │
          ▼
      Random Forest
          │
          ▼
    Phishing Detection
          │
          ▼
    Cybersecurity Analysis
          │
          ▼
        FastAPI
          │
          ▼
      Web Interface
```

---

## 🧰 Development Environment

| Component            | Technology |
|-----------------------|------------|
| Programming Language | Python |
| Backend              | FastAPI |
| Machine Learning     | Scikit-learn |
| Model                | Random Forest |
| Frontend             | HTML / CSS / JavaScript |
| Data Processing      | Pandas / NumPy |
| Visualization        | Matplotlib / Seaborn |
| Version Control      | Git / GitHub |
