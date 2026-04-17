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

Built an integrated analytics system combining:
- NLP-based sentiment classification  
- Intent detection  
- Escalation risk modeling  
- Time-series simulation for anomaly detection  
- Interactive dashboard for business decision-making  

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
