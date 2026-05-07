import streamlit as st
import pandas as pd


st.markdown("""
## 🚓 PatrolIQ

### Smart Crime Intelligence System

Transforming raw crime data into **actionable insights** using Machine Learning.
""")

st.markdown("---")

col1, col2, col3 = st.columns(3)

col1.markdown("### 📍 Hotspots\nIdentify high-risk crime zones")
col2.markdown("### ⏰ Temporal Patterns\nUnderstand when crimes occur")
col3.markdown("### 📊 Pattern Analysis\nExplore hidden structures")


st.set_page_config(page_title="PatrolIQ", layout="wide")

st.title("🚓 PatrolIQ - Smart Crime Intelligence Dashboard")

# ---------------- LOAD DATA ---------------- #
# df = pd.read_csv("../datasets/processed_datasets/clustered_data.csv")
# https://drive.google.com/file/d/1IoNg9sw-00GeFoTLIfYBEipR_X7Rdpt5/view?usp=sharing
import pandas as pd

file_id = "1IoNg9sw-00GeFoTLIfYBEipR_X7Rdpt5"

url = f"https://drive.google.com/uc?id={file_id}"

df = pd.read_csv(url)

# ---------------- KPIs ---------------- #
st.subheader("📊 Overall Insights")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Crimes", len(df))
col2.metric("Unique Crime Types", df["Primary Type"].nunique())
col3.metric("Clusters Identified", df["Cluster_KMeans"].nunique())
col4.metric("Most Common Crime", df["Primary Type"].mode()[0])

# ---------------- INTRO ---------------- #
st.markdown("""
### 🔍 What is PatrolIQ?

PatrolIQ is a data-driven crime analytics platform that helps identify:

- 📍 Crime hotspots using clustering
- ⏰ When crimes occur most frequently
- 📊 Hidden patterns in crime behavior

This system is designed to support decision-making for law enforcement.
""")

# ---------------- QUICK DISTRIBUTION ---------------- #
st.subheader("📊 Crime Distribution")

crime_counts = df["Primary Type"].value_counts().head(10)

st.bar_chart(crime_counts)

# ---------------- CLUSTER OVERVIEW ---------------- #
st.subheader("📍 Cluster Overview")

cluster_counts = df["Cluster_KMeans"].value_counts()

st.bar_chart(cluster_counts)

# ---------------- FOOTER ---------------- #
st.markdown("---")
st.markdown("Built using Machine Learning (Unsupervised Clustering) + Streamlit")