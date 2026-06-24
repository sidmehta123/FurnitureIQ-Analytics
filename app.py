import streamlit as st
import pandas as pd

# PAGE IMPORTS
import exec_summary
import descriptive
import clustering
import prediction
import prescriptive
import scorer

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="FurnitureIQ Analytics",
    page_icon="🛋️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🛋️ FurnitureIQ")
st.sidebar.caption("D2C Furniture Analytics Platform")

page = st.sidebar.radio(
    "Navigate",
    [
        "Executive Summary",
        "Descriptive Analysis",
        "Customer Segmentation",
        "Prediction Models",
        "Prescriptive Analysis",
        "Customer Scorer"
    ]
)

# Empty dataframe for now
df = pd.DataFrame()

# -----------------------------
# PAGE ROUTING
# -----------------------------
if page == "Executive Summary":
    exec_summary.show(df)

elif page == "Descriptive Analysis":
    descriptive.show(df)

elif page == "Customer Segmentation":
    clustering.show(df)

elif page == "Prediction Models":
    prediction.show(df)

elif page == "Prescriptive Analysis":
    prescriptive.show(df)

elif page == "Customer Scorer":
    scorer.show(df)
