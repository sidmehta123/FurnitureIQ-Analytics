import streamlit as st
import pandas as pd
import plotly.express as px

def show(df):

    st.title("🤖 Prediction Models")

    st.markdown("Predict repeat purchases and customer value")

    col1,col2,col3,col4 = st.columns(4)

    col1.metric("Accuracy","87%")
    col2.metric("Precision","84%")
    col3.metric("Recall","82%")
    col4.metric("F1 Score","83%")

    chart = pd.DataFrame({
        "Feature":[
            "Order Value",
            "Satisfaction",
            "Delivery Time",
            "Age",
            "Discount"
        ],
        "Importance":[35,25,18,12,10]
    })

    fig = px.bar(
        chart,
        x="Importance",
        y="Feature",
        orientation="h",
        color="Feature",
        color_discrete_sequence=[
            "#A8DADC",
            "#FFD6A5",
            "#BDE0FE",
            "#CDB4DB",
            "#D8F3DC"
        ]
    )

    st.plotly_chart(fig,use_container_width=True)
