import streamlit as st

def show(df):

    st.title("📊 Executive Summary")

    st.markdown("""
    Overview of the FurnitureIQ Analytics platform.
    """)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Customers", "2,000")

    with col2:
        st.metric("Cities Covered", "8")

    with col3:
        st.metric("Product Categories", "5")

    with col4:
        st.metric("Analytics Layers", "4")

    st.markdown("---")

    st.success("""
    FurnitureIQ Analytics helps a D2C furniture startup understand:

    • Customer behavior

    • Product demand

    • Marketing performance

    • Revenue opportunities

    • Future growth potential
    """)
