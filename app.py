import streamlit as st
import pandas as pd

import exec_summary
import descriptive
import clustering
import prediction
import prescriptive
import scorer

st.set_page_config(
    page_title="FurnitureIQ Analytics",
    page_icon="🛋️",
    layout="wide"
)

st.sidebar.title("🛋️ FurnitureIQ")

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

df = pd.DataFrame()

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
