import streamlit as st

# ← This must be your first Streamlit command, and only one!
st.set_page_config(
    page_title="Muneeb’s Portfolio",
    layout="wide",
    initial_sidebar_state="expanded"
)

import home
import projects
import contacts

st.sidebar.title("Navigate")
page = st.sidebar.radio(
    "",
    ("🏠 Home", "📊 Projects", "✉️ Contact"),
)

if page == "🏠 Home":
    home.run()
elif page == "📊 Projects":
    projects.run()
else:
    contacts.run()
