
import streamlit as st
import numpy as np
import pandas as pd
import joblib
from PIL import Image

# -------------------------------------------------
# Streamlit Page Configuration
# -------------------------------------------------
st.set_page_config(page_title="Student Depression Predictor", page_icon="🧠", layout="wide")

# Load Model
@st.cache_resource
def load_model():
    return joblib.load("AdaBoost_model.pkl")

model = load_model()

# -------------------------------------------------
# Custom CSS for Modern UI
# -------------------------------------------------
st.markdown(
    """
    <style>
    body {background: linear-gradient(135deg, #E3F3FF 0%, #FFFFFF 100%);}    

    .main-title {
        font-size: 48px;
        font-weight: 800;
        text-align: center;
        color: #2E8B57;
        margin-top: 10px;
    }

    .sub-title {
        font-size: 20px;
        text-align: center;
        color: #555;
        margin-bottom: 20px;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.45);
        backdrop-filter: blur(12px);
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
        margin-bottom: 25px;
    }

    .predict-button button {
        background: linear-gradient(to right, #2E8B57, #3CB371);
        color: white;
        font-size: 18px !important;
        font-weight: 600;
        height: 3.2em;
        border-radius: 12px;
        transition: 0.3s ease;
    }
    .predict-button button:hover {
        transform: scale(1.03);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------------------------------
# Sidebar
# -------------------------------------------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3209/3209995.png", width=120)
    st.title("🧠 Depression Predictor")
    st.markdown("Use lifestyle and behavioral data to estimate depression likelihood.")
    st.markdown("---")
    st.markdown("👨‍💻 Developer: **Swapnil Mishra**")
    st.markdown("🔗 GitHub: [Swapnil Mishra](https://github.com/SwapnilMishra29)")
    st.markdown("🔗 LinkedIn: [Profile](https://www.linkedin.com/in/swapnil-mishra70/)")
    st.markdown("---")
    st.markdown("✨ Explore the power of AI!")

# -------------------------------------------------
# Header Section
# -------------------------------------------------
st.markdown("<h1 class='main-title'>Student Depression Prediction 🧠</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='sub-title'>Fill in the student's lifestyle & academic details</h3>", unsafe_allow_html=True)

st.image('Artificial Intelligence Application in Mental Health Research copy.jpg', use_container_width=True)
st.markdown("<hr>", unsafe_allow_html=True)

# -------------------------------------------------
# Glassmorphic Input Form
# -------------------------------------------------
st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
st.markdown("### 📋 Student Details Form")

col1, col2 = st.columns(2)

with col1:
    id_val = st.number_input("Student ID", min_value=0, step=1)
    gender = st.radio("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=1, max_value=120)
    city = st.text_input("City")
    profession = st.text_input("Profession")
    academic_pressure = st.slider("Academic Pressure (1-5)", 1.0, 5.0, 3.0)
    study_satisfaction = st.slider("Study Satisfaction (1-5)", 1.0, 5.0, 3.0)
    sleep_duration = st.selectbox("Sleep Duration", [
        "Less than 5 hours", "5-6 hours", "7-8 hours", "More than 8 hours"
    ])

with col2:
    dietary_habits = st.radio("Dietary Habits", ["Healthy", "Unhealthy"])
    suicidal_thoughts = st.radio("Suicidal thoughts?", ["Yes", "No"])
    work_pressure = st.slider("Work Pressure (1-5)", 0.0, 5.0)
    financial_stress = st.slider("Financial Stress (1-5)", 1, 5, 3)
    family_history = st.radio("Family History of Illness?", ["Yes", "No"])
    job_satisfaction = st.slider("Job Satisfaction (1-5)", 0.0, 5.0)
    study_pressure_hours = st.number_input("Study/Work Hours per Week", min_value=0, max_value=24)
    cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.01)
    degree = st.text_input("Degree")

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------
# Category Mapping
# -------------------------------------------------
gender = 1 if gender == 'Male' else 0
dietary_habits = 1 if dietary_habits == 'Healthy' else 0
suicidal_thoughts = 1 if suicidal_thoughts == 'Yes' else 0
family_history = 1 if family_history == 'Yes' else 0

sleep_map = {'Less than 5 hours': 4, '5-6 hours': 5.5, '7-8 hours': 7.5, 'More than 8 hours': 9}
sleep_duration = sleep_map[sleep_duration]

# -------------------------------------------------
# Create Input DataFrame
# -------------------------------------------------
columns = [
    'id', 'Gender', 'Age', 'City', 'Profession', 'Academic Pressure',
    'Work Pressure', 'CGPA', 'Study Satisfaction', 'Job Satisfaction',
    'Sleep Duration', 'Dietary Habits', 'Degree',
    'Have you ever had suicidal thoughts ?', 'Work/Study Hours',
    'Financial Stress', 'Family History of Mental Illness'
]

input_df = pd.DataFrame([[id_val, gender, age, city, profession, academic_pressure,
                          work_pressure, cgpa, study_satisfaction, job_satisfaction,
                          sleep_duration, dietary_habits, degree, suicidal_thoughts,
                          study_pressure_hours, financial_stress, family_history]],
                        columns=columns)

# -------------------------------------------------
# Prediction Button
# -------------------------------------------------
st.markdown("<div class='predict-button'>", unsafe_allow_html=True)
predict = st.button("🔮 Predict Depression Level")
st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------
# Prediction Output
# -------------------------------------------------
if predict:
    with st.spinner("Analyzing student data..."):
        try:
            proba = model.predict_proba(input_df)
            depression_prob = proba[0][1]

            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            st.subheader("📊 Prediction Result")

            if depression_prob < 0.2:
                st.success("🟢 Very unlikely to have depression.")
            elif depression_prob < 0.4:
                st.success("🟢 Unlikely to have depression.")
            elif depression_prob < 0.6:
                st.warning("🟠 May have depression.")
            elif depression_prob < 0.8:
                st.warning("🟠 Likely to have depression.")
            else:
                st.error("🔴 Highly likely to have depression.")

            st.metric("Depression Probability", f"{depression_prob*100:.2f}%")
            st.markdown("</div>", unsafe_allow_html=True)

        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
