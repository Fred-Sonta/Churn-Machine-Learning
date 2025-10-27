# 📉 Customer Churn Prediction

Predict customer churn using Logistic Regression to identify at-risk customers before they leave.

## 🎯 Overview

Binary classification model that predicts whether a customer will churn (leave) or stay based on their behavior and demographics.

## ⚡ Quick Start

```bash
pip install pandas scikit-learn matplotlib
python churn_prediction.py
```

## 📊 Model Performance

- **Algorithm**: Logistic Regression
- **Accuracy**: ~80-85%
- **Key Metrics**: Precision, Recall, F1-Score, ROC-AUC

## 🔑 Key Features

- Customer demographics (age, tenure, contract type)
- Usage patterns (monthly charges, services subscribed)
- Account information (payment method, billing)

## 📈 Output

```
Churn Probability: 0.78 → High Risk ⚠️
Churn Probability: 0.15 → Low Risk ✅
```

## 🛠️ Pipeline

```
Data → Preprocessing → Train/Test Split → Logistic Regression → Evaluation → Predictions
```

## 💡 Use Case

Help businesses:
- Identify at-risk customers
- Target retention campaigns
- Reduce customer acquisition costs
- Improve customer lifetime value

