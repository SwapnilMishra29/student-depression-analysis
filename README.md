# Student Depression Analysis  
By Swapnil Mishra  

---

## Table of Contents  
- [Project Overview](#project-overview)  
- [Motivation](#motivation)  
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Architecture & Workflow](#architecture--workflow)  
- [Usage](#usage)  
- [Dataset](#dataset)  
- [Model & Methods](#model--methods)  
- [Results & Insights](#results--insights)  
- [Deployment](#deployment)  
- [Future Work](#future-work)  
- [Contributing](#contributing)  
- [License](#license)  
- [Contact](#contact)  

---

## Project Overview  
This project presents a web-based interactive analysis platform for understanding depression patterns among students. Using user-input features (e.g., study hours, sleep quality, social behaviour, etc.), the model estimates the likelihood of depression and highlights key influencing factors. The front-end is built with [Streamlit](https://streamlit.io) and enables quick insights through visualization and model predictions.

---

## Motivation  
Student mental health is a critical but often under-discussed topic. Many students may experience symptoms of depression without seeking help. By leveraging data science, this tool aims to:  
- Raise awareness of potential mental-health triggers in a student context  
- Provide an interactive, quick assessment to start a conversation  
- Highlight actionable factors like sleep, social interaction, academic pressure  

---

## Features  
- ✅ Interactive questionnaire to collect student-related behavioural and academic inputs  
- ✅ Real-time prediction of depression risk  
- ✅ Visualizations of feature relationships (e.g., correlation between sleep quality and depression risk)  
- ✅ Explanatory insights on which features contribute most to the prediction  
- ✅ Easy deployment via Streamlit for sharing and quick access  

---

## Tech Stack  
- **Frontend / Web App**: Streamlit  
- **Backend / Model**: Python (libraries: pandas, scikit-learn, numpy, matplotlib/seaborn)  
- **ML Model**: (e.g., Logistic Regression / Random Forest / XGBoost)  
- **Version Control & Deployment**: GitHub repository + Streamlit Cloud  
- **Data Visualization**: Seaborn / Matplotlib / Plotly  

---

## Architecture & Workflow  
1. **Data ingestion & preprocessing**: Clean raw student-survey dataset, handle missing values, encode categorical features.  
2. **Exploratory Data Analysis (EDA)**: Generate summary statistics, visualize distributions, check correlations.  
3. **Feature engineering**: Derive new features (e.g., sleep deficit, study vs leisure ratio).  
4. **Model training**: Split into train/test sets, train model(s), evaluate using metrics (accuracy, precision, recall, ROC-AUC).  
5. **Model deployment**: Save trained model (pickle or joblib), integrate into Streamlit app.  
6. **Web app interaction**: User fills form → Input features are mapped/preprocessed → Model predicts depression risk → App shows result + feature-importance visualization.  

---

## Usage  
**Prerequisites**  
```bash
pip install -r requirements.txt
Run locally

bash
Copy code
streamlit run app.py
Usage Instructions

Open the URL displayed (e.g., http://localhost:8501)

Fill in required fields (sleep hours, study hours, social interaction score, etc.)

Click “Predict” to see your estimated risk level and which factors influenced the result

Explore the “Insights” tab to view data visualizations

Dataset
The dataset consists of responses from students capturing features such as: sleep hours, daily screen time, study hours, extracurricular participation, social interaction rating, perceived academic pressure, etc.

All data is anonymized and collected (or simulated) for educational use only.

Feature list:

sleep_hours: Average sleep per night

study_hours: Average time spent studying per day

screen_time: Hours of screen usage (leisure + academic)

social_interaction: Self-rated on a scale of 1–5

academic_pressure: Self-rated on a scale of 1–5

is_depressed: Target variable (binary: 0 = No, 1 = Yes)

(Adapt the above list based on your actual dataset.)

Model & Methods
Model selection: After comparing several models, the best performing one was a Random Forest Classifier with hyperparameters: n_estimators=100, max_depth=5, random_state=42.

Evaluation metrics

Accuracy: ~ 85%

Precision: ~ 0.80

Recall: ~ 0.78

ROC-AUC: ~ 0.87

Feature Importance: Top features influencing depression risk were:

sleep_hours

social_interaction

academic_pressure

study_hours

screen_time

(Replace with your actual model, metrics and feature-importance results.)

Results & Insights
Students sleeping less than 6 hours had a significantly higher predicted risk of depression.

Lower social interaction scores correlated strongly with higher risk.

High academic pressure combined with low leisure time was another key risk pattern.

The interactive tool can help students quickly reflect on their habits and potentially seek help earlier.

Here’s a sample screenshot of the web app:

Deployment
Hosted live via Streamlit Community Cloud: Student Depression Analysis

To update:

Push changes to your GitHub repo

Streamlit automatically redeploys (or manually trigger redeploy)

Ensure model .pkl and necessary files are committed or stored via Git LFS / cloud storage as needed.

Future Work
Expand dataset with real student-survey responses (with proper ethics / consent)

Add more granular features (e.g., physical activity, dietary habits, mental-health history)

Incorporate a “recommendation” module (e.g., if high risk → show resources, helpline links)

Build a mobile-friendly version or publish as a PWA

Integrate longitudinal tracking (student fills weekly and tool shows progress/trend)

Contributing
Contributions are welcome! If you’d like to contribute:

Fork the repository

Create a new branch (git checkout -b feature-yourFeature)

Make your changes (code + tests + documentation)

Submit a Pull Request with a clear description of your change

Please ensure your code follows the existing style guidelines and is properly tested.

License
This project is licensed under the MIT License – see the LICENSE file for details.

Contact
Swapnil Mishra

GitHub: github.com/swapnilmishra

Email: yourname@example.com (replace with your actual email)

LinkedIn: linkedin.com/in/swapnilmishra

Thank you for visiting this project! I hope the tool adds value and sparks meaningful discussion around student mental-health.

yaml
Copy code

---

If you like, I can **generate a fully formatted README.md file** ready to drop into your repo, including badges (build, license), GIF screenshot, and code snippets. Do you want that?
::contentReference[oaicite:0]{index=0}
