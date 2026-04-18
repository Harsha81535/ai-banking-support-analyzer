# 🏦 AI Banking Support Analyzer

An end-to-end NLP and machine learning system designed to analyze banking customer support interactions, identify sentiment and intent, and predict escalation risk in real time.

---

## Key Highlights

- Processed and standardized multi-source banking datasets into a unified schema  
- Built NLP pipeline using TF-IDF + ensemble ML models (~81% accuracy)  
- Designed escalation risk prediction system using rule-based + meta-classifier approach  
- Simulated sentiment trends to detect spikes during outage-like scenarios  
- Developed an interactive Streamlit dashboard for business insights  

---

## 📸 Dashboard Preview

![Dashboard Overview](https://github.com/user-attachments/assets/947d3ddb-1b35-43ef-ae3d-98d9436c327a)

---

![Live Prediction](https://github.com/user-attachments/assets/c33aafab-d804-4166-b54d-b47b906f3b39)

---

![Trend Analysis](https://github.com/user-attachments/assets/51972db2-85d9-4e43-abf9-7239297d29bd)

---

## Problem Statement

Customer support systems in banking generate large volumes of unstructured text data. Identifying high-risk interactions manually is inefficient and reactive.

This project aims to:
- Automatically classify sentiment and intent  
- Identify high-risk interactions early  
- Enable proactive escalation handling  

---

## Solution

> End-to-end pipeline from raw multi-source data → NLP modeling → escalation prediction → interactive decision dashboard

Built an end-to-end analytics system through a structured pipeline:

### 1. Data Aggregation & Standardization  
- Combined multiple datasets (BANKING77, FiQA, Kaggle reviews, financial tweets)  
- Standardized into a unified schema: `text | intent | sentiment | source`  
- Cleaned and aligned inconsistent formats across sources  

---

### 2. Sentiment Enrichment (NLP)  
- Applied a RoBERTa-based model to generate sentiment labels  
- Augmented datasets lacking sentiment information  
- Standardized outputs into Positive / Neutral / Negative  

---

### 3. Feature Engineering  
- Transformed text using TF-IDF (bigrams, stopword removal)  
- Performed stratified train-test split  
- Optimized feature space (~6000 features)  

---

### 4. Sentiment Classification Model  
- Built an ensemble model using:
  - Logistic Regression  
  - Random Forest  
  - XGBoost  
- Combined predictions using soft voting  
- Achieved ~81% accuracy  

---

### 5. Escalation Risk Modeling  

**Rule-Based Layer**
- Assigned baseline risk by intent  
- Weighted sentiment probabilities to estimate risk  

**Meta-Classifier Layer**
- Trained Gradient Boosting model on:
  - sentiment probabilities  
  - intent risk  
- Predicted escalation levels: Low / Medium / High  

---

### 6. Time-Series Simulation  
- Simulated temporal behavior of customer interactions  
- Tracked daily sentiment and escalation trends  
- Implemented rolling averages and spike detection  
- Tested system response using outage-like scenarios  

---

### 7. Interactive Dashboard  
- Built a Streamlit dashboard for real-time insights  
- Features:
  - Sentiment distribution  
  - Intent–sentiment mapping  
  - Escalation risk visualization  
  - Live message testing  

---

### 8. Business Impact  
- Enabled early identification of high-risk interactions  
- Improved visibility into customer sentiment trends  
- Provided a decision-support tool for support teams  

---

## Features

- Real-time sentiment classification (Positive / Neutral / Negative)  
- Intent–sentiment correlation mapping  
- Escalation risk prediction (Low / Medium / High)  
- Sentiment trend visualization  
- Live message testing with instant predictions  

---

## Tech Stack

- Python (pandas, numpy, scikit-learn)  
- NLP: TF-IDF, Transformers (RoBERTa - conceptual pipeline)  
- Visualization: Streamlit  
- ML Models: Ensemble methods  
- Data Analysis: matplotlib, seaborn  

---

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Model Development & Analysis

The full model development workflow is documented in the notebook export:

[Download & View Analysis Notebook](analysis_notebook.html)

> To view: download the file and open it in your browser.

### This includes:
- Data preprocessing and dataset creation  
- NLP pipeline (RoBERTa + TF-IDF)  
- Ensemble model experimentation  
- Escalation risk modeling  
- Time-series simulation and trend analysis
## Use Case

Designed for banking and fintech organizations to:
- Identify high-risk customer interactions early
- Improve customer experience
- Enable proactive support and escalation handling

## Author
- Harshana Sriraman
- PGDM (Banking & Financial Services)
- Institute of Management Technology, Ghaziabad
