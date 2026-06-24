import streamlit as st
import pandas as pd
import plotly.express as px

def show(df):

```
# =====================================
# CUSTOM STYLING
# =====================================

st.markdown("""
<style>

.main {
    background-color:#FAF7F2;
}

.insight-box {
    background-color:#F5F0E6;
    padding:20px;
    border-radius:15px;
    border-left:8px solid #8B5E3C;
    margin-bottom:15px;
}

.section-header {
    color:#3E2C23;
    font-weight:600;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# HEADER
# =====================================

col1, col2 = st.columns([1,5])

with col1:
    try:
        st.image("logo.png", width=100)
    except:
        pass

with col2:
    st.title("🛋️ FurnitureIQ Analytics")
    st.caption("Executive Decision Intelligence Platform")

st.markdown("---")

st.header("📊 Executive Summary")

st.write("""
This dashboard provides a comprehensive overview of business performance,
customer behavior, acquisition effectiveness and growth opportunities
for the FurnitureIQ D2C Furniture Startup.
""")

st.markdown("")

# =====================================
# PRIMARY KPI CARDS
# =====================================

st.subheader("💰 Business Performance")

c1,c2,c3,c4 = st.columns(4)

c1.metric("Revenue", "₹3.8 Cr", "+12.4%")
c2.metric("Orders", "2,000", "+9.1%")
c3.metric("Avg Order Value", "₹19,250", "+6.2%")
c4.metric("Repeat Purchase", "37%", "+4.8%")

st.markdown("")

c5,c6,c7,c8 = st.columns(4)

c5.metric("Customer Growth", "+15%")
c6.metric("Avg Satisfaction", "4.2 / 5")
c7.metric("Return Rate", "8.3%")
c8.metric("Top Category", "Sofas")

st.markdown("---")

# =====================================
# REVENUE OVERVIEW
# =====================================

st.subheader("📈 Revenue Overview")

revenue_df = pd.DataFrame({
    "Category":[
        "Sofas",
        "Beds",
        "Dining Sets",
        "Storage Units",
        "Decor"
    ],
    "Revenue":[92,85,55,48,35]
})

fig = px.bar(
    revenue_df,
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
    paper_bgcolor="#FAF7F2",
    plot_bgcolor="#FAF7F2",
    showlegend=False,
    font_color="#3E2C23",
    height=450
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# =====================================
# CUSTOMER & CITY OVERVIEW
# =====================================

left,right = st.columns(2)

with left:

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
        "Revenue":[22,18,17,12,9,8,7,7]
    })

    fig2 = px.pie(
        city_df,
        names="City",
        values="Revenue",
        hole=0.55,
        color_discrete_sequence=[
            "#8B5E3C",
            "#A67C52",
            "#D8C3A5",
            "#C8B6A6",
            "#EADBC8",
            "#B08968",
            "#9C6644",
            "#7F5539"
        ]
    )

    fig2.update_layout(
        paper_bgcolor="#FAF7F2",
        font_color="#3E2C23"
    )

    st.plotly_chart(fig2, use_container_width=True)

with right:

    st.subheader("👥 Customer Mix")

    customer_df = pd.DataFrame({
        "Segment":[
            "Premium Buyers",
            "Frequent Buyers",
            "Budget Shoppers",
            "Occasional Buyers"
        ],
        "Customers":[420,610,580,390]
    })

    fig3 = px.bar(
        customer_df,
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

    fig3.update_layout(
        paper_bgcolor="#FAF7F2",
        plot_bgcolor="#FAF7F2",
        showlegend=False,
        font_color="#3E2C23"
    )

    st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")

# =====================================
# EXECUTIVE INSIGHTS
# =====================================

st.subheader("💡 Executive Insights")

st.markdown("""
<div class="insight-box">

<h4>Key Findings</h4>

<ul>
<li>Sofas contribute the highest revenue and profit potential.</li>
<li>Mumbai and Delhi account for nearly 40% of total revenue.</li>
<li>Referral customers have the strongest repeat purchase behavior.</li>
<li>Customers experiencing delivery delays are significantly less likely to reorder.</li>
<li>Tier 1 cities generate higher order values than Tier 2 markets.</li>
</ul>

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =====================================
# STRATEGIC PRIORITIES
# =====================================

st.subheader("🎯 Strategic Priorities")

st.success("""

Priority 1:
Expand Sofa and Bed inventory

Priority 2:
Increase Instagram and Referral marketing

Priority 3:
Improve delivery performance in Tier 2 cities

Priority 4:
Launch loyalty programs for high-value customers

Priority 5:
Focus expansion on Bengaluru, Pune and Jaipur

""")

st.markdown("---")

st.caption(
    "FurnitureIQ Analytics | Executive Decision Dashboard"
)
```
