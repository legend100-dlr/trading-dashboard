import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "

import streamlit as st
import pandas as pd
import yfinance as yf

from data.loader import load_asset
from core.signals import compute_signal
from core.indicators import williams_r

st.title("📊 Trading Dashboard")

# Load data
df = load_asset("SPY")

# VIX
vix = yf.download("^VIX", period="1mo")
vix_val = vix["Close"].iloc[-1].item()

# Indicators
df["WR"] = williams_r(df)

# Signal
signal = compute_signal(df, vix_val)
st.header("🚨 FINAL DECISION")

if signal == "RISK_OFF":
    st.error("BUY PUTS / DEFENSIVE")
    confidence = 0.8
else:
    st.success("NO TRADE")
    confidence = 0.6

st.write(f"Confidence: {round(confidence*100)}%")
wr = df["WR"].iloc[-1]

st.subheader("🎯 Timing")

if wr > -20:
    st.success("✅ Overbought → good short timing")
elif wr < -80:
    st.warning("⚠️ Oversold → watch for bounce")
else:
    st.info("Neutral")

# Final Decision
st.header("🚨 FINAL DECISION")

if signal == "RISK_OFF":
    st.error("BUY PUTS / DEFENSIVE")
else:
    st.success("NO TRADE")

# Show data
st.line_chart(df["Close"])
st.line_chart(df["WR"])