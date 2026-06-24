import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def show(df):

    # ==========================
    # THEME
    # ==========================

    st.markdown("""
    <style>

    .recommendation-box {
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

    st.header("🎯 Customer Scorer")

    st.caption(
        "Predict customer value and purchase potential"
    )

    st.markdown("---")

    # ==========================
    # INPUT FORM
    # ==========================

    st.subheader("📝 Enter Customer Details")

    col1, col2 = st.columns(2)

    with col1:

        age = st.slider(
            "Age",
            18,
            55,
            30
        )

        city_tier = st.selectbox(
            "City Tier",
            ["Tier 1","Tier 2"]
        )

        acquisition = st.selectbox(
            "Acquisition Channel",
            [
                "Instagram",
                "Google Search",
                "Referral",
                "Influencer",
                "Email"
            ]
        )

    with col2:

        product = st.selectbox(
            "Preferred Product",
            [
                "Bed",
                "Sofa",
                "Dining Set",
                "Storage Unit",
                "Decor"
            ]
        )

        budget = st.slider(
            "Expected Budget (₹)",
            5000,
            100000,
            25000
        )

        previous_orders = st.slider(
            "Previous Orders",
            0,
            10,
            1
        )

    st.markdown("---")

    # ==========================
    # SCORE BUTTON
    # ==========================

    if st.button("🚀 Score Customer"):

        # --------------------------
        # SIMULATED LOGIC
        # --------------------------

        score = 50

        if city_tier == "Tier 1":
            score += 10

        if acquisition == "Referral":
            score += 15

        if acquisition == "Instagram":
            score += 10

        if budget > 30000:
            score += 15

        if previous_orders > 2:
            score += 20

        score = min(score,100)

        # --------------------------
        # SEGMENT
        # --------------------------

        if score >= 85:
            segment = "Premium Buyer"
            clv = "₹85,000"
            recommendation = "Offer premium collections and loyalty membership."

        elif score >= 70:
            segment = "Frequent Buyer"
            clv = "₹60,000"
            recommendation = "Promote bundles and referral rewards."

        elif score >= 55:
            segment = "Occasional Buyer"
            clv = "₹30,000"
            recommendation = "Retarget with seasonal promotions."

        else:
            segment = "Budget Shopper"
            clv = "₹18,000"
            recommendation = "Focus on discounts and entry-level products."

        st.markdown("---")

        # ==========================
        # OUTPUT KPIs
        # ==========================

        st.subheader("📊 Customer Scorecard")

        col1,col2,col3 = st.columns(3)

        col1.metric(
            "Purchase Probability",
            f"{score}%"
        )

        col2.metric(
            "Predicted Segment",
            segment
        )

        col3.metric(
            "Estimated CLV",
            clv
        )

        st.markdown("---")

        # ==========================
        # GAUGE CHART
        # ==========================

        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=score,
                title={'text': "Purchase Probability"},
                gauge={
                    'axis': {'range': [0,100]},
                    'bar': {'color': "#8B5E3C"},
                    'steps': [
                        {'range':[0,50],'color':"#EADBC8"},
                        {'range':[50,75],'color':"#D8C3A5"},
                        {'range':[75,100],'color':"#A67C52"}
                    ]
                }
            )
        )

        fig.update_layout(
            paper_bgcolor="#FAF7F2",
            font_color="#3E2C23",
            height=450
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.markdown("---")

        # ==========================
        # BUSINESS RECOMMENDATION
        # ==========================

        st.subheader("💡 Recommended Action")

        st.markdown(f"""
        <div class="recommendation-box">

        <h4>{segment}</h4>

        <p>{recommendation}</p>

        <p><strong>Expected Customer Lifetime Value:</strong> {clv}</p>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

        st.success("""
        Recommended Next Step:

        • Prioritize high-score customers

        • Personalize product recommendations

        • Optimize marketing spend based on customer segment

        • Focus retention efforts on high CLV users
        """)

    st.markdown("---")

    # ==========================
    # BULK UPLOAD SECTION
    # ==========================

    st.subheader("📂 Future Customer Upload")

    uploaded_file = st.file_uploader(
        "Upload New Customer CSV",
        type=["csv"]
    )

    if uploaded_file:

        upload_df = pd.read_csv(uploaded_file)

        st.success(
            f"{len(upload_df)} customers uploaded successfully."
        )

        st.dataframe(
            upload_df.head(),
            use_container_width=True
        )

        st.info("""
        Future Version:

        Uploaded customers will automatically receive:

        • Purchase Probability Score

        • Segment Assignment

        • Predicted Customer Lifetime Value

        • Personalized Marketing Recommendation
        """)
