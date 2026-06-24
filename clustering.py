import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder, StandardScaler


def show(df):

    st.title("🧩 Customer Segmentation")
    st.markdown("Identify customer groups using K-Means Clustering")

    try:

        data = df.copy()

        # Encode categorical columns
        categorical_cols = [
            "Gender",
            "City_Tier",
            "Acquisition_Channel",
            "Product_Category",
            "Repeat_Purchase"
        ]

        for col in categorical_cols:
            if col in data.columns:
                le = LabelEncoder()
                data[col] = le.fit_transform(data[col].astype(str))

        features = [
            "Age",
            "Final_Order_Value",
            "Delivery_Time",
            "Customer_Satisfaction",
            "Previous_Orders"
        ]

        features = [f for f in features if f in data.columns]

        X = data[features]

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # Sidebar controls
        n_clusters = st.sidebar.slider(
            "Number of Clusters",
            min_value=2,
            max_value=6,
            value=4
        )

        kmeans = KMeans(
            n_clusters=n_clusters,
            random_state=42,
            n_init=10
        )

        data["Cluster"] = kmeans.fit_predict(X_scaled)

        st.markdown("### Cluster Distribution")

        cluster_counts = (
            data["Cluster"]
            .value_counts()
            .sort_index()
            .reset_index()
        )

        cluster_counts.columns = ["Cluster", "Customers"]

        fig_bar = px.bar(
            cluster_counts,
            x="Cluster",
            y="Customers",
            color="Cluster",
            title="Customers per Cluster",
            color_discrete_sequence=[
                "#A8DADC",
                "#FFD6A5",
                "#BDE0FE",
                "#CDB4DB",
                "#D8F3DC",
                "#FFC8DD"
            ]
        )

        fig_bar.update_layout(
            plot_bgcolor="white",
            paper_bgcolor="white"
        )

        st.plotly_chart(fig_bar, use_container_width=True)

        st.markdown("---")

        st.markdown("### Customer Segments")

        fig_scatter = px.scatter(
            data,
            x="Final_Order_Value",
            y="Customer_Satisfaction",
            color=data["Cluster"].astype(str),
            size="Previous_Orders",
            hover_data=[
                "Age",
                "Delivery_Time"
            ],
            title="Customer Segmentation Map",
            color_discrete_sequence=[
                "#A8DADC",
                "#FFD6A5",
                "#BDE0FE",
                "#CDB4DB",
                "#D8F3DC",
                "#FFC8DD"
            ]
        )

        fig_scatter.update_layout(
            plot_bgcolor="white",
            paper_bgcolor="white"
        )

        st.plotly_chart(fig_scatter, use_container_width=True)

        st.markdown("---")

        st.markdown("### Cluster Profiles")

        profile = (
            data.groupby("Cluster")[features]
            .mean()
            .round(2)
        )

        st.dataframe(
            profile,
            use_container_width=True
        )

        st.markdown("---")

        st.markdown("### Business Interpretation")

        for cluster in sorted(data["Cluster"].unique()):

            avg_order = (
                data[data["Cluster"] == cluster]
                ["Final_Order_Value"]
                .mean()
            )

            avg_sat = (
                data[data["Cluster"] == cluster]
                ["Customer_Satisfaction"]
                .mean()
            )

            st.info(
                f"""
                Cluster {cluster}

                • Avg Order Value: ₹{avg_order:,.0f}

                • Avg Satisfaction: {avg_sat:.1f}/5

                • Recommended Action:
                Target with personalized offers and category-specific campaigns.
                """
            )

    except Exception as e:
        st.error(f"Error in clustering page: {e}")
