import streamlit as st
import pandas as pd
from pathlib import Path



# df = pd.read_csv("../datasets/processed_datasets/clustered_data.csv")

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

file_path = (
    BASE_DIR
    / "datasets"
    / "processed_datasets"
    / "clustered_data.csv"
)

df = pd.read_csv(file_path)
# ---------------- PAGE TITLE ---------------- #
st.title("📈 Model Analysis & Insights")

st.markdown("""
This section explains how different clustering models performed 
and why the final model was selected.
""")

# ---------------- KPI SECTION ---------------- #
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Records", len(df))
col2.metric("Clusters (KMeans)", df["Cluster_KMeans"].nunique())
col3.metric("Features Used", 2)

# ---------------- MODEL COMPARISON ---------------- #
st.subheader("📊 Model Comparison")

model_data = pd.DataFrame({
    "Model": ["KMeans", "DBSCAN", "Hierarchical"],
    "Silhouette Score": [0.39, 0.56, 0.41],
    "Usability": ["High", "Low", "Medium"]
})

st.dataframe(model_data)

# Bar chart
st.subheader("📈 Score Comparison")

chart_data = model_data.set_index("Model")["Silhouette Score"]
st.bar_chart(chart_data)

# ---------------- DETAILED EXPLANATION ---------------- #
st.subheader("🧠 Model Breakdown")

st.markdown("""
### 🔹 KMeans (Final Model)
- Uses geographic coordinates for clustering
- Produces well-balanced clusters
- Covers the entire dataset
- Easy to interpret as crime hotspots

### 🔹 DBSCAN
- Identifies dense regions
- Produced very few clusters
- Most data points grouped into one cluster
- Not useful for identifying multiple hotspots

### 🔹 Hierarchical Clustering
- Shows meaningful structure
- Computationally expensive for large datasets
- Used only for analysis
""")

# ---------------- KEY INSIGHT ---------------- #
st.subheader("⚠️ Important Insight")

st.warning("""
A higher silhouette score does NOT always mean a better model.

DBSCAN achieved a higher score, but failed to produce meaningful 
clusters for this problem.

Interpretability and usefulness are more important than score alone.
""")

# ---------------- FINAL DECISION ---------------- #
st.subheader("✅ Final Model Selection")

st.success("""
KMeans using geographic features was selected as the final model 
because it provides clear, interpretable crime hotspot zones 
and works efficiently on large datasets.
""")

# ---------------- FOOTER ---------------- #
st.markdown("---")
st.markdown("🚀 PatrolIQ | Machine Learning Crime Analytics Dashboard")