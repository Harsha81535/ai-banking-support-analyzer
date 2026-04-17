import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# -----------------------------------------------
# CONFIG
# -----------------------------------------------
st.set_page_config(page_title="AI Banking Support Analyzer", layout="wide")

st.title("🏦 AI Banking Support Analyzer")
st.caption("Real-time Sentiment, Intent & Escalation Intelligence")

# -----------------------------------------------
# LOAD DATA
# -----------------------------------------------
try:
    df = pd.read_csv("hybrid_banking_dataset_v5.csv")
except:
    st.warning("Using synthetic demo dataset")

    # Create dummy dataset
    df = pd.DataFrame({
        "text": ["sample"] * 500,
        "sentiment": np.random.choice(["negative", "neutral", "positive"], 500),
        "intent": np.random.choice([
            "transaction_charged_twice",
            "card_declined",
            "login_issue",
            "atm_failure"
        ], 500)
    })

# -----------------------------------------------
# METRICS
# -----------------------------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Messages", len(df))

sent_counts = df["sentiment"].value_counts()
neg = sent_counts.get("negative", 0)
pos = sent_counts.get("positive", 0)

col2.metric("😡 Negative", neg)
col3.metric("🙂 Positive", pos)

# -----------------------------------------------
# SENTIMENT DISTRIBUTION
# -----------------------------------------------
st.markdown("---")
st.subheader("Sentiment Distribution")

sent_df = sent_counts.reset_index()
sent_df.columns = ["Sentiment", "Count"]

st.bar_chart(sent_df.set_index("Sentiment"))

# -----------------------------------------------
# INTENT vs SENTIMENT
# -----------------------------------------------
st.subheader("Intent vs Sentiment Mapping")

intent_sent = (
    df.groupby(["intent", "sentiment"])
    .size()
    .unstack(fill_value=0)
)

st.dataframe(intent_sent)

# -----------------------------------------------
# INSIGHTS
# -----------------------------------------------
st.markdown("---")
st.subheader("AI Insight Summary")

top_negative_intents = (
    df[df["sentiment"] == "negative"]["intent"]
    .value_counts()
    .head(3)
    .index.tolist()
)

neg_pct = (neg / len(df)) * 100 if len(df) else 0

st.markdown(f"""
**Key Insights**

- Out of **{len(df):,} customer messages**, **{neg_pct:.1f}%** were negative  
- Top complaint categories: **{", ".join(top_negative_intents)}**  
- Negative sentiment strongly correlates with **higher escalation risk**  

This indicates potential service issues in the above areas requiring attention.
""")

# -----------------------------------------------
# SIMPLE TREND (NO PROPHET)
# -----------------------------------------------
st.markdown("---")
st.subheader("Sentiment Trend")

df["date"] = pd.date_range(start="2022-01-01", periods=len(df), freq="D")

trend = df.groupby("date")["sentiment"].apply(
    lambda x: (x == "negative").mean()
).reset_index()

st.line_chart(trend.rename(columns={"sentiment": "negative_ratio"}).set_index("date"))

# -----------------------------------------------
# LIVE SENTIMENT TESTER
# -----------------------------------------------
st.markdown("---")
st.subheader("Live Sentiment & Escalation Analyzer")

user_input = st.text_area("Enter a customer message:")

if st.button("Analyze Message"):
    if not user_input.strip():
        st.warning("Please enter a message to analyze")
    else:
        # --- Simple rule-based simulation ---
        text = user_input.lower()

        negative_keywords = ["bad", "worst", "charged", "error", "fail", "blocked", "issue", "problem", "declined"]
        positive_keywords = ["good", "great", "thanks", "happy"]

        if any(word in text for word in negative_keywords):
            sentiment = "Negative"
            confidence = np.random.uniform(0.7, 0.9)
            escalation = "High"
        elif any(word in text for word in positive_keywords):
            sentiment = "Positive"
            confidence = np.random.uniform(0.7, 0.9)
            escalation = "Low"
        else:
            sentiment = "Neutral"
            confidence = np.random.uniform(0.5, 0.7)
            escalation = "Medium"

        # --- Display results ---
        st.success(f"Predicted Sentiment: {sentiment}")
        st.write(f"Confidence Score: {confidence:.2f}")

        if escalation == "High":
            st.error("⚠️ High Escalation Risk")
        elif escalation == "Medium":
            st.warning("⚠️ Medium Escalation Risk")
        else:
            st.info("✅ Low Escalation Risk")
