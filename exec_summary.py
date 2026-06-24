import streamlit as st

def show(df):
    st.title("📊 Executive Summary")

    st.markdown("### Business Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Customers", "2,000")

    with col2:
        st.metric("Cities Covered", "8")

    with col3:
        st.metric("Product Categories", "5")

    with col4:
        st.metric("Analytics Modules", "6")

    st.markdown("---")

    st.success("""
    FurnitureIQ Analytics helps identify:
    
    • Best-selling furniture categories
    
    • High-value customer segments
    
    • Most profitable cities
    
    • Top-performing acquisition channels
    
    • Customer retention opportunities
    """)
