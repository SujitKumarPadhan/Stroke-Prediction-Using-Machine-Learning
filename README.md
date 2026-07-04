# 🧠 Stroke Prediction Using Machine Learning

An end-to-end Machine Learning project that predicts the likelihood of stroke using patient healthcare data. This project includes data preprocessing, exploratory data analysis (EDA), machine learning model training, evaluation, and deployment using Streamlit.

---
## 📌 Project Overview

Stroke is one of the leading causes of death and long-term disability worldwide. Early prediction of stroke risk can help healthcare professionals take preventive actions and improve patient outcomes.

This project uses Machine Learning techniques to predict whether a patient is at risk of stroke based on demographic and medical information.

---
## 🎯 Objectives

- Predict stroke risk using Machine Learning.
- Perform Exploratory Data Analysis (EDA).
- Handle missing values and class imbalance.
- Compare K-Nearest Neighbors (KNN) and Gaussian Naive Bayes models.
- Deploy the trained model using Streamlit.

---

## 📂 Dataset Information

- **Dataset:** Healthcare Stroke Dataset
- **Total Records:** 5,110
- **Features:** 12
- **Target Variable:** Stroke
  - `0` = No Stroke
  - `1` = Stroke

### Features

- Gender
- Age
- Hypertension
- Heart Disease
- Ever Married
- Work Type
- Residence Type
- Average Glucose Level
- BMI
- Smoking Status
- Stroke

---

## 📊 Exploratory Data Analysis (EDA)

Key findings from the analysis:

- The dataset is highly imbalanced.
- Stroke risk increases with age.
- Hypertension and Heart Disease are positively associated with stroke.
- Average Glucose Level has a weak positive correlation with stroke.
- BMI shows a very weak correlation with stroke.
- No strong multicollinearity exists among the numerical features.

---

## ⚙️ Data Preprocessing

The following preprocessing steps were performed:

- Removed unnecessary **ID** column.
- Handled missing values in the **BMI** column.
- Applied **One-Hot Encoding** for categorical features.
- Standardized numerical features using **StandardScaler**.
- Used **ColumnTransformer** for preprocessing.
- Applied **SMOTE** to balance the dataset.
- Split the data into training and testing sets.

---

## 🤖 Machine Learning Models

Two machine learning models were implemented and compared:

### 1. K-Nearest Neighbors (KNN)
- Distance-based classification algorithm.
- Hyperparameters optimized using GridSearchCV.

### 2. Gaussian Naive Bayes
- Probability-based classification algorithm.
- Assumes feature independence.
- Used for performance comparison.

---
---

## 📈 Model Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC Score
- Confusion Matrix
- Classification Report

### Performance Comparison

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|--------|---------:|----------:|--------:|---------:|---------:|
| KNN | 85.81% | 16.26% | 32.26% | 21.62% | 64.24% |
| Gaussian Naive Bayes | 81.51% | 18.41% | 59.68% | 28.14% | 83.00% |

---

## 🌐 Streamlit Web Application

https://stroke-prediction-using-machine-learning-kmpaabiiphj9ygghyogdk.streamlit.app/

### Features

- User-friendly interface
- Patient information input form
- Real-time stroke risk prediction
- Instant prediction results

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- SMOTE (Imbalanced-learn)
- Streamlit
- Joblib
- VS Code

---

## 🚀 Future Improvements

- Improve prediction accuracy using advanced machine learning models.
- Integrate deep learning techniques.
- Deploy the application on a cloud platform.
- Integrate with hospital management systems.
- Enhance the user interface and add explainable AI features.

---

## 👨‍💻 Author

**Sujit Kumar Padhan**

Machine Learning Enthusiast

---

⭐ If you found this project useful, please consider giving it a star on GitHub!












