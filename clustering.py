import streamlit as st
import pandas as pd
import plotly.express as px

def show(df):

    st.title("🧩 Customer Segmentation")

    st.markdown("Customer clusters based on purchasing behavior")

    data = pd.DataFrame({
        "OrderValue":[10000,15000,25000,35000],
        "Satisfaction":[3,4,5,5],
        "Segment":[
            "Budget Buyers",
            "Regular Buyers",
            "Premium Buyers",
            "VIP Customers"
        ]
    })

    fig = px.scatter(
        data,
        x="OrderValue",
        y="Satisfaction",
        color="Segment",
        size="OrderValue",
        color_discrete_sequence=[
            "#A8DADC",
            "#FFD6A5",
            "#BDE0FE",
            "#CDB4DB"
        ]
    )

    st.plotly_chart(fig,use_container_width=True)
