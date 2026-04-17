# ai-banking-support-analyzer
NLP + ML system for banking support sentiment &amp; escalation analysis
# AI Banking Support Analyzer

An end-to-end NLP and machine learning system designed to analyze customer support interactions in the banking domain, identify sentiment and intent, and predict escalation risk.

## Overview
This project integrates multiple public banking-related datasets into a unified schema and builds a robust analytics pipeline for:
- Sentiment classification
- Intent detection
- Escalation risk prediction
- Time-series trend analysis

## Key Features
- NLP pipeline using RoBERTa and TF-IDF features
- Ensemble machine learning models for sentiment classification (~81% accuracy)
- Rule-based + meta-classifier approach for escalation prediction
- Time-series simulation to detect spikes (e.g., outage scenarios)
- Interactive Streamlit dashboard for business insights

## Dashboard Highlights
- Key support metrics (positive/neutral/negative sentiment)
- Intent–sentiment correlation analysis
- Escalation trend visualization
- Real-time message sentiment & risk prediction

## Tech Stack
- Python (pandas, numpy, scikit-learn)
- NLP: transformers (RoBERTa)
- Visualization: Streamlit
- ML Models: Gradient Boosting, ensemble methods

## How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
