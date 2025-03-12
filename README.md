# Loan-Approval-Prediction
The Loan Approval Prediction System is a machine learning-based web application that predicts whether a loan application will be approved or rejected based on applicant details. It is built using Python, Streamlit, and Scikit-Learn and uses a K-Nearest Neighbors (KNN) classifier to make predictions.
Here is a **README.md** file for your Loan Approval Prediction project. 🚀  

---

### **📜 README.md**
```markdown
# 🏦 Loan Approval Prediction System

This is a **machine learning-based web application** that predicts **loan approval** based on applicant details.  
The project is built using **Python, Streamlit, and Scikit-Learn**.

---

## 🚀 **Project Overview**
The **Loan Approval Prediction System** uses **K-Nearest Neighbors (KNN)** to classify loan applications as **approved** or **not approved**.  
It processes user inputs, scales the data, and uses a trained model to make predictions.

---

## 📂 **Project Structure**
```
Loan_Approval_Prediction/
│── app.py                   # Streamlit web app
│── Loan_Approval_pred_model.ipynb   # Jupyter notebook for model training
│── loan.csv.xlsx             # Dataset (Loan applicant details)
│── model.pkl                 # Trained ML model (KNeighborsClassifier)
│── scaler.pkl                # StandardScaler for feature scaling
│── target_label_encoder.pkl   # Label encoder for loan status (Y/N)
│── README.md                 # Project documentation (this file)
```

---

## 📌 **Installation & Setup**
### **1️⃣ Install Dependencies**
Ensure you have Python installed, then install required packages:
```bash
pip install streamlit pandas scikit-learn openpyxl
```

### **2️⃣ Run the Streamlit Web App**
```bash
streamlit run app.py
```
🔹 This will open the web app in your browser.

---

## 🏗 **How It Works**
1. **User inputs loan details** (income, loan amount, credit history, etc.).
2. **Data is preprocessed** (categorical encoding, missing value handling, and scaling).
3. **The trained ML model predicts** whether the loan is **approved (✅) or rejected (❌).**
4. **Prediction is displayed in the web interface.**

---

## 📊 **Machine Learning Model**
- **Algorithm Used**: K-Nearest Neighbors (KNN)
- **Dataset**: `loan.csv.xlsx`
- **Feature Scaling**: StandardScaler
- **Encoding**: Label Encoding for categorical values

---

## 🛠 **Model Training (Jupyter Notebook)**
To retrain the model, open `Loan_Approval_pred_model.ipynb` and run:
```python
# Train and save the model
from sklearn.neighbors import KNeighborsClassifier
import pickle

model = KNeighborsClassifier()
model.fit(X_scaled, y)

# Save the model
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)
```
🔹 Replace the old `model.pkl` if retraining is required.

---

## 🏆 **Features**
✅ User-friendly **Streamlit Web App**  
✅ **Handles Missing Values** (Mean/Most Frequent Imputation)  
✅ **Encodes Categorical Data** (Gender, Married, Property Area, etc.)  
✅ **Feature Scaling** using StandardScaler  
✅ **Trained ML Model** for accurate predictions  

---

## 🖥 **Screenshots**
📌 **Main Web App Interface**  
![Loan Approval Prediction App](https://via.placeholder.com/600x300?text=Loan+Approval+Prediction+App)

---

## 📜 **License**
This project is open-source and available for modification and improvements. 🎉

---

## connect ##
LinkedIN:https://www.linkedin.com/in/rashmirm/

 

---
🎯 **Happy Coding & Predicting!** 🚀
`
---

📢 **Let me know if you need any modifications! 🚀🔥**
