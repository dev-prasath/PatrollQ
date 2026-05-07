import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.decomposition import PCA


st.title("📊 PCA Crime Pattern Visualization")

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


st.markdown("""
### 🧠 What is PCA?

PCA reduces complex data into 2 dimensions while preserving patterns.
Each point represents a crime instance.
Clusters show grouping behavior.
""")

df = df.sample(5000, random_state=42).reset_index(drop=True)

features = [
    "Lat_scaled","Long_scaled","Hour","Month",
    "Is_Weekend","Crime_Severity",
    "Primary_Type_Encoded","Location_Encoded"
]

X = df[features]

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

df_pca = pd.DataFrame(X_pca, columns=["PC1", "PC2"])
df_pca["Cluster"] = df["Cluster_KMeans"]

fig = px.scatter(
    df_pca,
    x="PC1",
    y="PC2",
    color="Cluster",
    title="Cluster Separation in PCA Space"
)

st.plotly_chart(fig)

st.markdown("""
### Insight:
Clusters are partially separable, indicating meaningful grouping of crime patterns.
""")