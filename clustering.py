import streamlit as st
import pandas as pd
import plotly.express as px

def show(df):

    # ==========================
    # THEME
    # ==========================

    st.markdown("""
    <style>

    .persona-card {
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

    st.header("🧩 Customer Segmentation")

    st.caption(
        "Grouping customers based on purchasing behavior and engagement"
    )

    st.markdown("")

    # ==========================
    # KPI SECTION
    # ==========================

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Customers", "2,000")
    col2.metric("Segments Identified", "4")
    col3.metric("Avg Order Value", "₹19,250")
    col4.metric("Repeat Purchase Rate", "37%")

    st.markdown("---")

    # ==========================
    # SEGMENT DISTRIBUTION
    # ==========================

    st.subheader("👥 Customer Segment Distribution")

    segment_df = pd.DataFrame({
        "Segment":[
            "Premium Buyers",
            "Budget Shoppers",
            "Frequent Buyers",
            "Occasional Buyers"
        ],
        "Customers":[420,580,610,390]
    })

    fig = px.bar(
        segment_df,
        x="Segment",
        y="Customers",
        color="Segment",
        color_discrete_sequence=[
            "#8B5E3C",
            "#A67C52",
            "#D8C3A5",
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
    # CUSTOMER MAP
    # ==========================

    st.subheader("🎯 Customer Value Map")

    scatter_df = pd.DataFrame({
        "Order Value":[15000,9000,22000,12000],
        "Satisfaction":[4.6,3.7,4.8,4.0],
        "Segment":[
            "Premium Buyers",
            "Budget Shoppers",
            "Frequent Buyers",
            "Occasional Buyers"
        ],
        "Size":[120,180,220,140]
    })

    fig2 = px.scatter(
        scatter_df,
        x="Order Value",
        y="Satisfaction",
        size="Size",
        color="Segment",
        color_discrete_sequence=[
            "#8B5E3C",
            "#A67C52",
            "#D8C3A5",
            "#EADBC8"
        ]
    )

    fig2.update_layout(
        paper_bgcolor="#FAF7F2",
        plot_bgcolor="#FAF7F2",
        font_color="#3E2C23"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.markdown("---")

    # ==========================
    # PERSONA CARDS
    # ==========================

    st.subheader("🧠 Customer Personas")

    st.markdown("""
    <div class="persona-card">

    <h4>💎 Premium Buyers</h4>

    • High income customers

    • Highest order values

    • Low price sensitivity

    • Interested in premium furniture collections

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="persona-card">

    <h4>🛒 Budget Shoppers</h4>

    • Price-conscious buyers

    • Respond strongly to discounts

    • Lower average order value

    • High acquisition through promotions

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="persona-card">

    <h4>🔄 Frequent Buyers</h4>

    • Highest repeat purchase rate

    • Strong customer loyalty

    • Ideal for membership programs

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="persona-card">

    <h4>📦 Occasional Buyers</h4>

    • Purchase infrequently

    • Require re-engagement campaigns

    • Potential growth segment

    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ==========================
    # SEGMENT PERFORMANCE
    # ==========================

    st.subheader("📊 Average Order Value by Segment")

    perf_df = pd.DataFrame({
        "Segment":[
            "Premium Buyers",
            "Budget Shoppers",
            "Frequent Buyers",
            "Occasional Buyers"
        ],
        "Order Value":[35000,11000,24000,15000]
    })

    fig3 = px.bar(
        perf_df,
        x="Segment",
        y="Order Value",
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
    # RECOMMENDATIONS
    # ==========================

    st.subheader("🚀 Strategic Recommendations")

    st.success("""
    • Launch premium furniture collections for Premium Buyers.

    • Use discount campaigns for Budget Shoppers.

    • Create loyalty rewards for Frequent Buyers.

    • Run retargeting campaigns for Occasional Buyers.

    • Personalize marketing communication by segment.
    """)

    st.caption(
        "FurnitureIQ Analytics | Customer Segmentation Dashboard"
    )
