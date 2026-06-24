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
# PASTEL THEME
# -----------------------------
st.markdown("""
<style>

.stApp {
    background-color: #f8fbf8;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #ffffff;
    border-right: 1px solid #e5e7eb;
}

/* Main headings */
h1, h2, h3 {
    color: #1f2937;
}

/* Metric cards */
[data-testid="stMetric"] {
    background-color: #eef7f0;
    border-radius: 12px;
    padding: 15px;
    text-align: center;
}

/* Buttons */
.stButton>button {
    background-color: #95d5b2;
    color: black;
    border-radius: 10px;
    border: none;
}

/* Dataframes */
[data-testid="stDataFrame"] {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# LOAD DATA
# -----------------------------
try:
    df = pd.read_csv("furniture_dataset.csv")
except:
    df = pd.DataFrame()

# -----------------------------
# SIDEBAR
# -----------------------------
try:
    st.sidebar.image("logo.png", width=120)
except:
    pass

st.sidebar.markdown("## 🛋️ FurnitureIQ")
st.sidebar.caption("D2C Furniture Analytics Platform")

st.sidebar.markdown("---")

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

# -----------------------------
# HOME IF NO DATA
# -----------------------------
if df.empty:

    st.title("🛋️ FurnitureIQ Analytics")

    st.markdown("""
    ## MBA Data Analytics Project

    A complete analytics platform for a D2C Furniture Startup.

    ### Features

    - Executive Dashboard
    - Descriptive Analytics
    - Customer Segmentation
    - Predictive Models
    - Prescriptive Analytics
    - Customer Scoring

    Upload the dataset to begin analysis.
    """)

    st.stop()

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
