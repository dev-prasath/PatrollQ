import streamlit as st
import pandas as pd
import plotly.express as px

from pathlib import Path



st.title("📍 Crime Hotspot Explorer")

# df = pd.read_csv("../datasets/processed_datasets/clustered_data.csv")

BASE_DIR = Path(__file__).resolve().parent.parent.parent

file_path = (
    BASE_DIR
    / "datasets"
    / "processed_datasets"
    / "clustered_data.csv"
)

df = pd.read_csv(file_path)

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Hour"] = df["Date"].dt.hour

df = df.sample(7000, random_state=42).reset_index(drop=True)

# ---------------- FILTERS (MAIN AREA) ---------------- #
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("🔎 Filters")
# filters here

st.markdown('</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

crime_types = col1.multiselect(
    "Crime Type",
    df["Primary Type"].unique(),
    default=df["Primary Type"].unique()
)

clusters = col2.multiselect(
    "Cluster",
    sorted(df["Cluster_KMeans"].unique()),
    default=sorted(df["Cluster_KMeans"].unique())
)

hour_range = col3.slider("Hour Range", 0, 23, (0, 23))

# ---------------- FILTER DATA ---------------- #
df_filtered = df[
    (df["Primary Type"].isin(crime_types)) &
    (df["Cluster_KMeans"].isin(clusters)) &
    (df["Hour"] >= hour_range[0]) &
    (df["Hour"] <= hour_range[1])
]

# ---------------- EMPTY CASE ---------------- #
if df_filtered.empty:
    st.warning("No data for selected filters")

    fig = px.scatter_mapbox(lat=[], lon=[])
    fig.update_layout(mapbox_style="open-street-map")

    st.plotly_chart(fig)
    st.stop()

# ---------------- KPIs ---------------- #
st.subheader("📊 Insights")

c1, c2, c3 = st.columns(3)

c1.metric("Total Crimes", len(df_filtered))
c2.metric("Top Crime", df_filtered["Primary Type"].mode()[0])
c3.metric("Top Cluster", int(df_filtered["Cluster_KMeans"].mode()[0]))

# ---------------- MAP ---------------- #
st.markdown("### 🗺️ Crime Hotspots (Live View)")
fig = px.scatter_mapbox(
    df_filtered,
    lat="Latitude",
    lon="Longitude",
    color="Cluster_KMeans",
    hover_data=["Primary Type", "Hour"],
    zoom=10,
    height=600
)

st.markdown("""
### 🧠 Cluster Meaning

- Each color represents a crime hotspot
- Dense clusters indicate high-risk areas
- Useful for patrol planning
""")

fig.update_layout(mapbox_style="open-street-map")

st.plotly_chart(fig, use_container_width=True)

# ---------------- CLUSTER BREAKDOWN ---------------- #
st.subheader("📊 Cluster Distribution")

cluster_counts = df_filtered["Cluster_KMeans"].value_counts().reset_index()
cluster_counts.columns = ["Cluster", "Count"]

fig_bar = px.bar(cluster_counts, x="Cluster", y="Count", text="Count")

st.plotly_chart(fig_bar, use_container_width=True)

# ---------------- INSIGHT ---------------- #
st.subheader("🔥 Key Insight")

st.info(f"""
Cluster {int(df_filtered['Cluster_KMeans'].mode()[0])} is the most active hotspot.

Dominant crime: {df_filtered['Primary Type'].mode()[0]}
""")