import plotly.express as px

def cluster_distribution(df):
    dist = df["Cluster_Label"].value_counts(normalize=True).reset_index()
    dist.columns = ["Cluster", "Percentage"]

    fig = px.bar(
        dist,
        x="Cluster",
        y="Percentage",
        color="Cluster",
        title="Cluster Distribution (%)"
    )
    return fig


def temporal_hour_chart(df):
    hourly = df.groupby("Hour").size().reset_index(name="Crime_Count")

    fig = px.line(
        hourly,
        x="Hour",
        y="Crime_Count",
        title="Crime by Hour"
    )
    return fig


def risk_ranking(df):
    grouped = df.groupby("Cluster_Label").agg({
        "Crime_Severity": "mean",
        "Is_Night": "mean",
        "Arrest": "mean",
        "Latitude": "count"
    }).rename(columns={"Latitude": "Crime_Count"})

    grouped["Risk_Score"] = (
        grouped["Crime_Severity"] * 0.5 +
        grouped["Is_Night"] * 0.3 +
        (1 - grouped["Arrest"]) * 0.2
    )

    grouped = grouped.sort_values(by="Risk_Score", ascending=False)

    fig = px.bar(
        grouped,
        x=grouped.index,
        y="Risk_Score",
        title="Risk Ranking by Cluster"
    )

    return fig, grouped