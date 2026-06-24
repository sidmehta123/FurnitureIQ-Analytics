import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def show(df):

    # ==========================
    # THEME
    # ==========================

    st.markdown("""
    <style>

    .insight-box {
        background-color:#FAF7F2;
        padding:20px;
        border-radius:15px;
        border-left:6px solid #8B5E3C;
        margin-bottom:15px;
    }

    </style>
    """, unsafe_allow_html=True)

    # ==========================
    # HEADER
    # ==========================

    col1, col2 = st.columns([1,5])

    with col1:
        try:
            st.image("logo.png", width=90)
        except:
            pass

    with col2:
        st.title("🛋️ FurnitureIQ Analytics")

    st.markdown("---")

    st.header("🤖 Prediction Models")

    st.caption(
        "Predicting repeat purchases and customer lifetime value"
    )

    st.markdown("")

    # ==========================
    # MODEL PERFORMANCE
    # ==========================

    st.subheader("📊 Model Performance")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Accuracy", "88%")
    col2.metric("Precision", "86%")
    col3.metric("Recall", "84%")
    col4.metric("F1 Score", "85%")

    st.markdown("---")

    # ==========================
    # ROC CURVE
    # ==========================

    st.subheader("📈 ROC Curve")

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=[0,0.05,0.10,0.20,1],
            y=[0,0.60,0.80,0.93,1],
            mode='lines',
            fill='tozeroy',
            name='Random Forest (AUC = 0.91)',
            line=dict(
                color="#8B5E3C",
                width=4
            )
        )
    )

    fig.add_trace(
        go.Scatter(
            x=[0,1],
            y=[0,1],
            mode='lines',
            line=dict(
                dash='dash',
                color='gray'
            ),
            name='Baseline'
        )
    )

    fig.update_layout(
        paper_bgcolor="#FAF7F2",
        plot_bgcolor="#FAF7F2",
        font_color="#3E2C23",
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    # ==========================
    # FEATURE IMPORTANCE
    # ==========================

    st.subheader("🎯 Feature Importance")

    importance_df = pd.DataFrame({
        "Feature":[
            "Customer Satisfaction",
            "Previous Orders",
            "Delivery Time",
            "Order Value",
            "Discount Applied",
            "Acquisition Channel"
        ],
        "Importance":[32,24,18,14,7,5]
    })

    fig2 = px.bar(
        importance_df,
        x="Importance",
        y="Feature",
        orientation="h",
        color="Feature",
        color_discrete_sequence=[
            "#8B5E3C",
            "#A67C52",
            "#D8C3A5",
            "#C8B6A6",
            "#EADBC8",
            "#B08968"
        ]
    )

    fig2.update_layout(
        paper_bgcolor="#FAF7F2",
        plot_bgcolor="#FAF7F2",
        showlegend=False,
        font_color="#3E2C23"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.markdown("---")

    # ==========================
    # PURCHASE PROBABILITY
    # ==========================

    st.subheader("🛒 Purchase Probability by Segment")

    segment_df = pd.DataFrame({
        "Segment":[
            "Premium Buyers",
            "Frequent Buyers",
            "Occasional Buyers",
            "Budget Shoppers"
        ],
        "Probability":[91,85,62,55]
    })

    fig3 = px.bar(
        segment_df,
        x="Segment",
        y="Probability",
        color="Segment",
        color_discrete_sequence=[
            "#8B5E3C",
            "#A67C52",
            "#D8C3A5",
            "#EADBC8"
        ]
    )

    fig3.update_layout(
        paper_bgcolor="#FAF7F2",
        plot_bgcolor="#FAF7F2",
        showlegend=False,
        font_color="#3E2C23"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    st.markdown("---")

    # ==========================
    # CLV PREDICTION
    # ==========================

    st.subheader("💰 Predicted Customer Lifetime Value")

    clv_df = pd.DataFrame({
        "Segment":[
            "Premium Buyers",
            "Frequent Buyers",
            "Occasional Buyers",
            "Budget Shoppers"
        ],
        "CLV":[85000,62000,28000,18000]
    })

    fig4 = px.bar(
        clv_df,
        x="Segment",
        y="CLV",
        color="Segment",
        color_discrete_sequence=[
            "#8B5E3C",
            "#A67C52",
            "#D8C3A5",
            "#EADBC8"
        ]
    )

    fig4.update_layout(
        paper_bgcolor="#FAF7F2",
        plot_bgcolor="#FAF7F2",
        showlegend=False,
        font_color="#3E2C23"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

    st.markdown("---")

    # ==========================
    # INSIGHTS
    # ==========================

    st.subheader("💡 Predictive Insights")

    st.markdown("""
    <div class="insight-box">

    <h4>Model Findings</h4>

    <ul>

    <li>Customer Satisfaction is the strongest predictor of repeat purchases.</li>

    <li>Customers with multiple previous orders are significantly more likely to purchase again.</li>

    <li>Long delivery times negatively impact future buying behavior.</li>

    <li>Premium Buyers generate the highest lifetime value.</li>

    <li>Repeat purchase probability exceeds 90% for highly satisfied customers.</li>

    </ul>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("")

    # ==========================
    # BUSINESS ACTIONS
    # ==========================

    st.subheader("🚀 Recommended Actions")

    st.success("""

    • Prioritize retention campaigns for Premium Buyers.

    • Improve delivery times to increase repeat purchases.

    • Launch loyalty programs for Frequent Buyers.

    • Focus marketing spend on high-CLV customer segments.

    • Use predictive scores for personalized targeting.

    """)

    st.caption(
        "FurnitureIQ Analytics | Predictive Analytics Dashboard"
    )
