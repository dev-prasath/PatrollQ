# 🚓 PatrolIQ – Smart Crime Analytics Dashboard

PatrolIQ is a data-driven crime analytics system that uses **unsupervised machine learning** to identify crime hotspots, analyze temporal patterns, and provide actionable insights through an interactive dashboard.

---

## 📌 Project Overview

This project analyzes large-scale crime data to uncover:

- 📍 Crime hotspots using clustering
- ⏰ Time-based crime patterns
- 📊 Hidden relationships using dimensionality reduction
- 📈 Actionable insights for decision-making

> ⚠️ This is **not a prediction system**.  
> It focuses on **pattern discovery and insights** using unsupervised learning.

---

## 🧠 Key Objectives

- Identify high-risk geographic zones
- Understand when crimes occur most frequently
- Visualize complex crime patterns
- Build an interactive dashboard for exploration

---

## ⚙️ Tech Stack

- **Python**
- **Pandas, NumPy**
- **Scikit-learn**
- **Matplotlib, Seaborn, Plotly**
- **Streamlit**

---

## 🗂️ Project Structure
PatrolIQ/
│
├── datasets/
│ ├── raw_datasets/
│ └── processed_datasets/
│
├── notebooks/
│ ├── data_preprocessing.ipynb
│ ├── feature_engineering.ipynb
│ ├── clustering.ipynb
│ └── dimensionality_reduction.ipynb
│
├── app/
│ ├── main.py
│ ├── pages/
│ │ ├── hotspots.py
│ │ ├── temporal_analysis.py
│ │ ├── pca_visualization.py
│ │ └── model_metrics.py
│
├── requirements.txt
└── README.md


---

## 🔄 Workflow
Raw Data
↓
Data Preprocessing
↓
Feature Engineering
↓
Clustering (KMeans, DBSCAN, Hierarchical)
↓
Dimensionality Reduction (PCA, t-SNE)
↓
Streamlit Dashboard


---

## 🤖 Machine Learning Approach

### 🔹 Unsupervised Learning

- No target variable
- No prediction
- Focus on grouping patterns

---

### 🔹 Models Used

| Model        | Purpose              | Result |
|-------------|--------------------|--------|
| KMeans      | Hotspot detection   | ✅ Final Model |
| DBSCAN      | Density clustering  | ❌ Not suitable |
| Hierarchical| Structure analysis  | ⚠️ Supporting |

---

### 📊 Model Selection

- **KMeans (Geo-based)** was selected as the final model
- Uses only **latitude & longitude**
- Produces clear and interpretable clusters

---

### ⚠️ Important Insight

> A higher silhouette score does not always mean better clustering.  
> Interpretability and usefulness are more important.

---

## 📊 Features Engineered

- Hour, Day, Month
- Weekend indicator
- Crime severity score
- Encoded crime types
- Scaled geographic coordinates

---

## 📉 Dimensionality Reduction

- **PCA** → Understand feature importance
- **t-SNE** → Visual cluster separation

---

## 📍 Streamlit Dashboard Features

### 🔥 Crime Hotspots
- Interactive map with clustering
- Filters by crime type, cluster, and time
- Real-time insights

### ⏰ Temporal Analysis
- Hourly and daily crime trends
- Heatmap visualization
- Weekend vs weekday analysis

### 📊 PCA Visualization
- 2D representation of high-dimensional data
- Cluster distribution

### 📈 Model Insights
- Model comparison
- Final model justification

---

## 🚀 How to Run

### 1️⃣ Install dependencies
pip install -r requirements.txt


---

### 2️⃣ Run the app

cd app
streamlit run main.py


---

## 📊 Sample Insights

- Crimes peak during evening hours
- Certain clusters represent high-density crime zones
- Weekend crime activity is significantly higher

---

## 🎯 Use Cases

- Law enforcement planning
- Resource allocation
- Crime pattern analysis
- Urban safety research

---

## 🧠 Key Takeaway

> This project transforms raw crime data into a **decision-support system** using machine learning and visualization.

---

## 📌 Future Improvements

- Real-time data integration
- Predictive modeling (optional extension)
- Advanced geospatial analytics
- Deployment with cloud services

---

## 👨‍💻 Author

**Dev Prasath**

---

## ⭐ If you found this useful

Give a ⭐ on GitHub and share your feedback!

