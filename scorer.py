import streamlit as st

def show(df):

    st.title("🎯 Customer Scorer")

    age = st.number_input("Age",18,60,30)

    income = st.selectbox(
        "Income Level",
        ["Low","Medium","High"]
    )

    if st.button("Predict Customer Score"):

        st.metric(
            "Purchase Probability",
            "78%"
        )

        st.metric(
            "Expected Customer Value",
            "₹25,000"
        )

        st.success(
            "Recommended Segment: Premium Buyer"
        )
