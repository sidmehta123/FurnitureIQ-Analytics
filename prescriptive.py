import streamlit as st

def show(df):

    st.title("🚀 Prescriptive Analysis")

    st.markdown("Recommended actions based on insights")

    st.success("""
    Recommendation 1
    
    Increase marketing spend on Instagram Ads.
    """)

    st.info("""
    Recommendation 2
    
    Focus on Sofa and Bed categories.
    """)

    st.warning("""
    Recommendation 3
    
    Improve delivery speed in Tier 2 cities.
    """)
