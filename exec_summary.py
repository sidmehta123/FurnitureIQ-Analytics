import streamlit as st
import pandas as pd
import plotly.express as px


def show(df):

    # ==========================
    # CUSTOM THEME
    # ==========================

    st.markdown("""
    <style>

    .metric-card {
        background-color: #F5F0E6;
        padding: 15px;
        border-radius: 15px;
        text-align:center;
        border:1px solid #D8C3A5;
    }

    .insight-box {
        background-color:#FAF7F2;
        padding:20px;
        border-radius:15px;
        border-left:6px solid #8B5E3C;
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
        st.caption("Data-Driven Insights for D2C Furniture Growth")

    st.markdown("---")

    st.header("📊 Executive Summary")

    st.write("""
    This dashboard provides a strategic overview of customer behavior,
    product performance, acquisition effectiveness and revenue opportunities
    for the FurnitureIQ D2C Furniture Startup.
    """)

    st.markdown("")

    # ==========================
    # KPI SECTION
    # ==========================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Customers",
            "2,000"
        )

    with col2:
        st.metric(
            "Revenue",
            "₹3.8 Cr"
        )

    with col3:
        st.metric(
            "Avg Order Value",
            "₹19,250"
        )

    with col4:
        st.metric(
            "Repeat Purchase Rate",
            "37%"
        )

    st.markdown("---")

    # ==========================
    # CATEGORY REVENUE
    # ==========================

    st.subheader("🪑 Revenue by Product Category")

    category_df = pd.DataFrame({
        "Category":[
            "Beds",
            "Sofas",
            "Dining Sets",
            "Storage Units",
            "Decor"
        ],
        "Revenue":[85,92,55,48,35]
    })

    fig = px.bar(
        category_df,
        x="Category",
        y="Revenue",
        color="Category",
        color_discrete_sequence=[
            "#8B5E3C",
            "#A67C52",
            "#D8C3A5",
            "#C8B6A6",
            "#EADBC8"
        ]
    )

    fig.update_layout(
        plot_bgcolor="#FAF7F2",
        paper_bgcolor="#FAF7F2",
        font_color="#3E2C23",
        showlegend=False,
        title=""
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    # ==========================
    # CITY REVENUE
    # ==========================

    st.subheader("🏙️ Revenue Contribution by City")

    city_df = pd.DataFrame({
        "City":[
            "Mumbai",
            "Delhi",
            "Bengaluru",
            "Pune",
            "Jaipur",
            "Indore",
            "Lucknow",
            "Surat"
        ],
        "Revenue":[22,18,17,12,9,8,7,7]
    })

    fig2 = px.pie(
        city_df,
        values="Revenue",
        names="City",
        hole=0.45,
        color_discrete_sequence=[
            "#8B5E3C",
            "#A67C52",
            "#D8C3A5",
            "#C8B6A6",
            "#EADBC8",
            "#B08968",
            "#7F5539",
            "#9C6644"
        ]
    )

    fig2.update_layout(
        paper_bgcolor="#FAF7F2",
        font_color="#3E2C23"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.markdown("---")

    # ==========================
    # KEY INSIGHTS
    # ==========================

    st.subheader("💡 Key Business Insights")

    st.markdown("""
    <div class="insight-box">

    <h4>Top Findings</h4>

    <ul>
    <li>Sofas contribute the highest revenue among all categories.</li>
    <li>Mumbai and Delhi together account for nearly 40% of total sales.</li>
    <li>Tier 1 cities generate significantly higher order values.</li>
    <li>Customers with faster deliveries show higher repeat purchase rates.</li>
    <li>Referral customers demonstrate stronger long-term retention.</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("")

    # ==========================
    # STRATEGIC RECOMMENDATIONS
    # ==========================

    st.subheader("🚀 Strategic Recommendations")

    col1, col2 = st.columns(2)

    with col1:

        st.success("""
        **Marketing Strategy**

        • Increase Instagram and Referral campaigns

        • Focus acquisition in Tier 1 cities

        • Promote premium sofa collections
        """)

    with col2:

        st.info("""
        **Operational Strategy**

        • Reduce delivery times

        • Improve last-mile logistics

        • Expand high-margin product categories
        """)

    st.markdown("---")

    st.caption(
        "FurnitureIQ Analytics | Executive Dashboard"
    )
