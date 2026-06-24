import streamlit as st
import pandas as pd
import plotly.express as px

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

    st.header("📈 Descriptive Analysis")

    st.caption(
        "Understanding customer demographics, purchasing patterns and business performance"
    )

    st.markdown("")

    # ==========================
    # KPI CARDS
    # ==========================

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Customers", "2,000")
    col2.metric("Avg Age", "31")
    col3.metric("Avg Order Value", "₹19,250")
    col4.metric("Avg Satisfaction", "4.2/5")

    st.markdown("---")

    # ==========================
    # AGE DISTRIBUTION
    # ==========================

    st.subheader("👥 Customer Age Distribution")

    age_df = pd.DataFrame({
        "Age Group":[
            "18-25",
            "26-35",
            "36-45",
            "46-55"
        ],
        "Customers":[420,880,510,190]
    })

    fig = px.bar(
        age_df,
        x="Age Group",
        y="Customers",
        color="Age Group",
        color_discrete_sequence=[
            "#8B5E3C",
            "#A67C52",
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

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # ==========================
    # PRODUCT CATEGORY
    # ==========================

    st.subheader("🪑 Product Preferences")

    product_df = pd.DataFrame({
        "Category":[
            "Beds",
            "Sofas",
            "Dining Sets",
            "Storage Units",
            "Decor"
        ],
        "Orders":[540,620,390,280,170]
    })

    fig2 = px.pie(
        product_df,
        names="Category",
        values="Orders",
        hole=0.45,
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
        font_color="#3E2C23"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")

    # ==========================
    # REVENUE BY CITY
    # ==========================

    st.subheader("🏙️ Revenue by City")

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
        "Revenue":[55,48,42,28,18,14,13,11]
    })

    fig3 = px.bar(
        city_df,
        x="City",
        y="Revenue",
        color="Revenue",
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

    st.plotly_chart(fig3, use_container_width=True)

    st.markdown("---")

    # ==========================
    # ACQUISITION CHANNELS
    # ==========================

    st.subheader("📢 Acquisition Channel Performance")

    channel_df = pd.DataFrame({
        "Channel":[
            "Instagram",
            "Google",
            "Referral",
            "Influencer",
            "Email"
        ],
        "Customers":[650,510,390,260,190]
    })

    fig4 = px.bar(
        channel_df,
        x="Channel",
        y="Customers",
        color="Channel",
        color_discrete_sequence=[
            "#8B5E3C",
            "#A67C52",
            "#D8C3A5",
            "#C8B6A6",
            "#EADBC8"
        ]
    )

    fig4.update_layout(
        paper_bgcolor="#FAF7F2",
        plot_bgcolor="#FAF7F2",
        font_color="#3E2C23",
        showlegend=False
    )

    st.plotly_chart(fig4, use_container_width=True)

    st.markdown("---")

    # ==========================
    # SATISFACTION ANALYSIS
    # ==========================

    st.subheader("⭐ Satisfaction by City Tier")

    sat_df = pd.DataFrame({
        "Tier":["Tier 1","Tier 2"],
        "Satisfaction":[4.4,3.8]
    })

    fig5 = px.bar(
        sat_df,
        x="Tier",
        y="Satisfaction",
        color="Tier",
        color_discrete_sequence=[
            "#8B5E3C",
            "#D8C3A5"
        ]
    )

    fig5.update_layout(
        paper_bgcolor="#FAF7F2",
        plot_bgcolor="#FAF7F2",
        showlegend=False,
        font_color="#3E2C23"
    )

    st.plotly_chart(fig5, use_container_width=True)

    st.markdown("---")

    # ==========================
    # KEY INSIGHTS
    # ==========================

    st.subheader("💡 Key Findings")

    st.markdown("""
    <div class="insight-box">

    <h4>Business Insights</h4>

    <ul>
    <li>Sofas are the most demanded category and generate the highest revenue.</li>

    <li>Mumbai and Delhi contribute the largest share of overall revenue.</li>

    <li>Instagram is the strongest acquisition channel for customer growth.</li>

    <li>Tier 1 cities show significantly higher spending and satisfaction levels.</li>

    <li>Customers aged 26–35 form the largest buyer segment.</li>

    </ul>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("")

    st.subheader("🎯 Recommended Actions")

    st.success("""
    • Increase marketing spend on Instagram campaigns.

    • Focus expansion efforts on Tier 1 metro cities.

    • Prioritize Sofa and Bed inventory.

    • Improve customer experience in Tier 2 regions.

    • Introduce loyalty programs for repeat buyers.
    """)
