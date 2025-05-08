# streamlit_portfolio/projects.py
import streamlit as st
from streamlit.components.v1 import iframe

def run():
    st.header("📊 Projects")

    st.subheader("US Airlines Dashboard")
    tableau_url = (
        "https://public.tableau.com/views/USAirlineDashboard/USAirLinesDashBoard"
        "?:showVizHome=no&:toolbar=yes&:embed=true"
    )
    iframe(tableau_url, width=1120, height=727)

    # add more projects below if you like
