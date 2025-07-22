# 🫀 Heart Disease Prediction Model

A machine learning web app that predicts the likelihood of heart disease based on patient medical data. Built with **Streamlit**, trained on the **UCI Heart Disease dataset**, and deployed on **Streamlit Cloud**.

---

## 📌 Demo

👉 [Try the Live App]([https://your-app-link.streamlit.app](https://heartdiseasepredictionmodel-ebdzxhmphqeyztxnmaedhd.streamlit.app/))  

---

## 📂 Project Structure

heart_disease_prediction_model/
│
├── ui/
│ ├── app.py # Streamlit UI script
│ └── final_model.pkl # Trained ML model
│
├── data/ # Dataset files
│
├── requirements.txt # Python dependencies
└── README.md # You're here

markdown
Copy
Edit

---

## 📊 Dataset

- **Source:** [UCI Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/heart+Disease)
- **Features used:**
  - `age`, `sex`, `cp` (chest pain), `trestbps`, `chol`, `fbs`, `restecg`, `thalach`, `exang`, `oldpeak`, `slope`, `ca`, `thal`

- **Target:**
  - 1 → Has heart disease  
  - 0 → No heart disease

---

## 🤖 Model Details

- **Model:** Random Forest Classifier  
- **Libraries:** scikit-learn, pandas, numpy, joblib  
- **Training notebook:** Done in Jupyter

---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/zyad-elkhewekh/heart_disease_prediction_model.git
cd heart_disease_prediction_model
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run the Streamlit app
bash
Copy
Edit
cd ui
streamlit run app.py
🧠 Prediction Input
The app asks users to input:

Age

Gender

Chest Pain Type

Blood Pressure

Cholesterol Level

Fasting Blood Sugar

ECG Results

Max Heart Rate

Exercise-Induced Angina

ST Depression

Slope of ST Segment

Number of Major Vessels

Thalassemia Status

⚠️ All inputs are required for a prediction.

📦 Dependencies
streamlit

pandas

numpy

scikit-learn

joblib


📝 License
This project is open-source and free to use for educational or non-commercial purposes.

