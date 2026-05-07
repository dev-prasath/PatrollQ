import streamlit as st
import pandas as pd
import plotly.express as px



st.title("⏰ Temporal Crime Analysis")

# df = pd.read_csv("../datasets/processed_datasets/clustered_data.csv")

import pandas as pd

file_id = "1IoNg9sw-00GeFoTLIfYBEipR_X7Rdpt5"

url = f"https://drive.google.com/uc?id={file_id}"

df = pd.read_csv(url)
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Hour"] = df["Date"].dt.hour
df["Day"] = df["Date"].dt.day_name()

df = df.sample(10000, random_state=42)

# ---------------- KPIs ---------------- #
st.subheader("📊 Time Insights")

c1, c2, c3 = st.columns(3)

c1.metric("Peak Hour", df.groupby("Hour").size().idxmax())
c2.metric("Peak Day", df["Day"].value_counts().idxmax())
c3.metric("Weekend Crimes", int(df["Is_Weekend"].sum()))

# ---------------- HOURLY ---------------- #
st.subheader("📈 Crimes by Hour")

hourly = df.groupby("Hour").size().reset_index(name="Count")
st.plotly_chart(px.line(hourly, x="Hour", y="Count"))

# ---------------- DAY ---------------- #
st.subheader("📅 Crimes by Day")

day = df["Day"].value_counts().reset_index()
day.columns = ["Day", "Count"]

st.plotly_chart(px.bar(day, x="Day", y="Count"))

# ---------------- HEATMAP ---------------- #
st.subheader("🔥 Crime Heatmap")

pivot = df.pivot_table(index="Day", columns="Hour", aggfunc="size", fill_value=0)

fig = px.imshow(
    pivot,
    labels=dict(x="Hour", y="Day", color="Crime Count")
)

fig.update_traces(
    hovertemplate="Day: %{y}<br>Hour: %{x}<br>Crimes: %{z}"
)

st.plotly_chart(fig)

# ---------------- WEEKEND VS WEEKDAY ---------------- #
st.subheader("📊 Weekend vs Weekday")

weekend = df.groupby("Is_Weekend").size().reset_index(name="Count")
weekend["Type"] = weekend["Is_Weekend"].map({0: "Weekday", 1: "Weekend"})

st.plotly_chart(px.pie(weekend, names="Type", values="Count"))