# projects.py

import streamlit as st
import pandas as pd
from streamlit.components.v1 import iframe
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier


def run():
    st.title("📚 My Projects")

    # 1. Tableau Dashboards
    st.subheader("🔗 Tableau Dashboards")
    st.write("Interactive dashboards created with Tableau Public:")
    # ───────────────────────────────────────────────────────
    # Example embed (replace URL with yours):
    tableau_urls = {
        "US Airlines Dashboard": "https://public.tableau.com/views/USAirlineDashboard/USAirLinesDashBoard?:showVizHome=no&:toolbar=yes&:embed=true",
        # "British Airways Review": "https://public.tableau.com/shared/J4CPX2K4Q?:display_count=n&:origin=viz_share_link",
        # "Global Super Store Sales Dashboard": "https://public.tableau.com/views/GlobalSuperStoreSalesDashboard_17265669742860/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link",
        # add more as you remember them
    }
    for name, url in tableau_urls.items():
        st.markdown(f"**{name}**")
        iframe(url, width=900, height=600)
        st.markdown("---")


    # 2. Dash App
    st.subheader("🎛 Dash App")
    st.write("A Plotly Dash application for … (brief description)")
    st.markdown("- **Live demo:** [Link to Dash app](#)")
    st.markdown("- **Source code:** [GitHub repo](#)")
    st.markdown("---")


    # 2. Streamlit Apps
    st.title("🎓 College Placement Predictor")
    st.markdown("Predict your placement chances based on **CGPA** and **IQ**.")
    # Load dataset
    plc_df = pd.read_csv("datasets/placement-dataset.csv")

    # Fix: Use correct features
    X = plc_df[['cgpa', 'iq']]
    y = plc_df['placement']

    # Split and train the model
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)
    model = LogisticRegression()
    model.fit(x_train, y_train)

    # Accuracy (for info)
    acc = accuracy_score(y_test, model.predict(x_test)) * 100
    st.info(f"Model Accuracy on Test Set: {acc:.1f}%")

    # User Input
    st.header("Select your parameters")
    st.write("Use the sliders to select your **CGPA** and **IQ** score.")

    cgpa = st.slider("CGPA", 0.0, 4.0, 3.0, 0.1)
    iq = st.slider("IQ Score", 0, 150, 100)

    # Prediction
    if st.button("Predict Placement"):
        input_df = pd.DataFrame({'cgpa': [cgpa], 'iq': [iq]})
        result = model.predict(input_df)[0]
        if result == 1:
            st.success("✅ Likely to be Placed")
        else:
            st.error("❌ Not Likely to be Placed")

    # Show data
    if st.checkbox("Show Training Data for Placement Prediction"):
        st.subheader("Training Data")
        st.write(plc_df)
        
    st.markdown("---")
    
    # 4. Crop Recommendation System
    st.title("🌾 Crop Recommendation System")
    st.markdown("Predict the best crop to grow based on **N**, **P**, **K**, **temperature**, **humidity**, **ph** and **rainfall**.")

    # Load dataset
    crop_df = pd.read_csv("datasets/crop_recommendation.csv")
    
    # Round off decimal columns
    decimal_cols = ['temperature', 'humidity', 'ph', 'rainfall']

    crop_df[decimal_cols] = crop_df[decimal_cols].round(2)
    
    X = crop_df.drop(columns=['label'])
    y = crop_df['label']
    
    # Split and train the model
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)
    model = RandomForestClassifier()
    
    model.fit(x_train, y_train)
    # Accuracy (for info)
    acc = accuracy_score(y_test, model.predict(x_test))
    # Accuracy percentage
    acc = acc * 100
    st.info(f"Model Accuracy on Test Set: {acc:.1f}%")
    
    # User Input
    st.header("Select your parameters")
    st.write("Use the sliders to select your **N**, **P**, **K**, **temperature**, **humidity**, **ph** and **rainfall**.")
    
    n = st.slider("N", 0, 200, 100)
    p = st.slider("P", 0, 200, 100)
    k = st.slider("K", 0, 200, 100)
    temperature = st.slider("Temperature", 0.0, 50.0, 25.0, 0.1)
    humidity = st.slider("Humidity", 0.0, 100.0, 50.0, 0.1)
    ph = st.slider("pH", 0.0, 14.0, 7.0, 0.1)
    rainfall = st.slider("Rainfall", 0.0, 300.0, 150.0, 0.1)
    
    
    # Prediction
    if st.button("Predict Crop"):
        input_df = pd.DataFrame({'N': [n], 'P': [p], 'K': [k], 'temperature': [temperature], 'humidity': [humidity], 'ph': [ph], 'rainfall': [rainfall]})
        result = model.predict(input_df)[0]
        st.success(f"✅ Recommended Crop: {result}")
        st.balloons()
    
    if st.checkbox("Show Training Data for Crop Recommendation"):
        st.subheader("Training Data")
        st.write(crop_df)
        
    st.markdown("---")