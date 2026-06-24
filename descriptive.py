import streamlit as st
import pandas as pd
import plotly.express as px

def show(df):

    st.title("📈 Descriptive Analysis")

    st.markdown("Understand customer demographics and purchasing behavior")

    col1,col2,col3,col4 = st.columns(4)

    col1.metric("Customers", "2000")
    col2.metric("Avg Age", "31")
    col3.metric("Avg Order Value", "₹18,500")
    col4.metric("Avg Satisfaction", "4.2")

    st.markdown("---")

    sample = pd.DataFrame({
        "Category":["Beds","Sofas","Dining Sets","Storage","Decor"],
        "Orders":[520,480,350,410,240]
    })

    fig = px.bar(
        sample,
        x="Category",
        y="Orders",
        color="Category",
        color_discrete_sequence=[
            "#A8DADC",
            "#FFD6A5",
            "#BDE0FE",
            "#CDB4DB",
            "#D8F3DC"
        ]
    )

    st.plotly_chart(fig,use_container_width=True)
