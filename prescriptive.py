import streamlit as st
import pandas as pd
import plotly.express as px

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

    st.header("🚀 Prescriptive Analysis")

    st.caption(
        "Strategic recommendations derived from descriptive, clustering and predictive analytics"
    )

    st.markdown("")

    # ==========================
    # KPI CARDS
    # ==========================

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Revenue Opportunity", "₹1.2 Cr")
    col2.metric("High Value Customers", "420")
    col3.metric("Retention Opportunity", "+18%")
    col4.metric("Return Reduction Potential", "-12%")

    st.markdown("---")

    # ==========================
    # MARKETING PRIORITY
    # ==========================

    st.subheader("📢 Marketing Budget Allocation")

    marketing_df = pd.DataFrame({
        "Channel":[
            "Instagram",
            "Referral",
            "Google Search",
            "Influencer",
            "Email"
        ],
        "Budget %":[
            35,
            25,
            20,
            12,
            8
        ]
    })

    fig = px.bar(
        marketing_df,
        x="Channel",
        y="Budget %",
        color="Channel",
        color_discrete_sequence=[
            "#8B5E3C",
            "#A67C52",
            "#D8C3A5",
            "#C8B6A6",
            "#EADBC8"
        ]
    )

    fig.update_layout(
        paper_bgcolor="#FAF7F2",
        plot_bgcolor="#FAF7F2",
        showlegend=False,
        font_color="#3E2C23"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    # ==========================
    # PRODUCT FOCUS
    # ==========================

    st.subheader("🪑 Product Expansion Priorities")

    product_df = pd.DataFrame({
        "Category":[
            "Sofas",
            "Beds",
            "Dining Sets",
            "Storage Units",
            "Decor"
        ],
        "Priority Score":[
            95,
            88,
            76,
            61,
            42
        ]
    })

    fig2 = px.bar(
        product_df,
        x="Category",
        y="Priority Score",
        color="Category",
        color_discrete_sequence=[
            "#8B5E3C",
            "#A67C52",
            "#D8C3A5",
            "#C8B6A6",
            "#EADBC8"
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
    # CITY EXPANSION
    # ==========================

    st.subheader("🏙️ Recommended Expansion Cities")

    city_df = pd.DataFrame({
        "City":[
            "Mumbai",
            "Delhi",
            "Bengaluru",
            "Pune",
            "Jaipur",
            "Indore"
        ],
        "Expansion Score":[
            98,
            94,
            91,
            84,
            76,
            70
        ]
    })

    fig3 = px.bar(
        city_df,
        x="City",
        y="Expansion Score",
        color="Expansion Score",
        color_continuous_scale=[
            "#EADBC8",
            "#D8C3A5",
            "#A67C52",
            "#8B5E3C"
        ]
    )

    fig3.update_layout(
        paper_bgcolor="#FAF7F2",
        plot_bgcolor="#FAF7F2",
        font_color="#3E2C23"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    st.markdown("---")

    # ==========================
    # CUSTOMER STRATEGY
    # ==========================

    st.subheader("👥 Segment Strategy Matrix")

    strategy_df = pd.DataFrame({
        "Segment":[
            "Premium Buyers",
            "Frequent Buyers",
            "Occasional Buyers",
            "Budget Shoppers"
        ],
        "Expected ROI":[
            95,
            88,
            61,
            52
        ]
    })

    fig4 = px.bar(
        strategy_df,
        x="Segment",
        y="Expected ROI",
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
    # CEO RECOMMENDATIONS
    # ==========================

    st.subheader("💡 Executive Recommendations")

    st.markdown("""
    <div class="recommendation-box">

    <h4>Recommendation 1</h4>

    Increase Instagram and Referral marketing investment since these channels generate the highest quality customers and strongest repeat purchase behavior.

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="recommendation-box">

    <h4>Recommendation 2</h4>

    Prioritize Sofa and Bed categories as they contribute the largest share of revenue and customer demand.

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="recommendation-box">

    <h4>Recommendation 3</h4>

    Reduce delivery times in Tier 2 cities to improve satisfaction and increase repeat purchases.

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="recommendation-box">

    <h4>Recommendation 4</h4>

    Launch loyalty and membership programs targeting Premium Buyers and Frequent Buyers to maximize Customer Lifetime Value.

    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ==========================
    # FINAL STRATEGY
    # ==========================

    st.subheader("🎯 Strategic Roadmap")

    st.success("""

    SHORT TERM (0–6 Months)

    • Increase Instagram marketing budget

    • Improve delivery efficiency

    • Optimize product inventory


    MEDIUM TERM (6–12 Months)

    • Expand in Tier 1 metro cities

    • Launch loyalty programs

    • Improve referral campaigns


    LONG TERM (1–3 Years)

    • Expand into Tier 2 growth markets

    • Launch private-label furniture collections

    • Build AI-powered recommendation engine

    """)

    st.caption(
        "FurnitureIQ Analytics | Prescriptive Decision Dashboard"
    )
