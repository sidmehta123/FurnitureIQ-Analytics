import streamlit as st

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="FurnitureIQ Analytics",
    page_icon="🛋️",
    layout="wide"
)

# -----------------------------
# CUSTOM STYLING
# -----------------------------
st.markdown("""
<style>
.main {
    background-color: #f8fafc;
}

h1 {
    color: #1f2937;
}

.metric-card {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.title("🛋️ FurnitureIQ Analytics")
st.subheader("MBA Data Analytics Project")

st.markdown("---")

# -----------------------------
# PROJECT OVERVIEW
# -----------------------------
st.markdown("""
## Welcome

FurnitureIQ Analytics is a data-driven platform designed for a Direct-to-Consumer (D2C) Furniture Startup.

The objective of this project is to use analytics to answer critical business questions:

- Which furniture categories generate the highest revenue?
- Which cities drive the most demand?
- Which marketing channels convert best?
- What causes returns and low satisfaction?
- How does delivery impact repeat purchases?
- Which customers are most valuable?

""")

st.markdown("---")

# -----------------------------
# KPI SECTION
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Target Dataset", "2,000 Customers")

with col2:
    st.metric("Cities Covered", "8")

with col3:
    st.metric("Product Categories", "5")

with col4:
    st.metric("Analytics Layers", "4")

st.markdown("---")

# -----------------------------
# ANALYTICS ROADMAP
# -----------------------------
st.markdown("""
## Analytics Framework

### 📊 Descriptive Analytics
Understand sales, customers, products, and channels.

### 🔍 Diagnostic Analytics
Identify causes of returns, low satisfaction, and churn.

### 🤖 Predictive Analytics
Predict purchase intent, repeat purchases, and customer value.

### 🚀 Prescriptive Analytics
Recommend actions for growth, marketing allocation, and expansion.
""")

st.markdown("---")

# -----------------------------
# STATUS
# -----------------------------
st.success("✅ Deployment Successful")

st.info("Next step: Upload dataset and build analytics pages.")
