import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import streamlit as st
import pandas as pd
import yfinance as yf

from data.loader import load_asset
from core.signals import compute_signal
from core.indicators import williams_r

st.title("📊 Trading Dashboard")

ticker = st.selectbox(
    "Select Asset",
    ["SPY", "QQQ", "ES=F"]
)

st.markdown(
    f"""
    <div style='padding:10px;border-radius:8px;background-color:#f0f2f6'>
        <strong>📊 Current Ticker:</strong> {ticker}
    </div>
    """,
    unsafe_allow_html=True
)

# Load data
df = load_asset(ticker)

# VIX
vix = yf.download("^VIX", period="1mo")
vix_val = vix["Close"].iloc[-1].item()

# Indicators
df["WR"] = williams_r(df)

# Signal
signal = compute_signal(df, vix_val)


# Debug section

st.subheader("Debug")

st.write(f"VIX: {vix_val}")

st.write(f"Last Close: {df['Close'].iloc[-1]}")

st.write(f"MA50: {df['MA50'].iloc[-1]}")

st.header("🏛 PORTFOLIO REGIME")

regime = signal["portfolio_regime"]
warning = signal["bear_warning"]
confidence = signal["confidence"]

if "AGGRESSIVE" in regime:
    st.success(regime)
elif "MODERATE" in regime:
    st.info(regime)
else:
    st.warning(regime)

st.subheader("⚠️ Bear Market Warning")

if warning == "LOW RISK":
    st.success(warning)
elif warning == "BUILDING RISK":
    st.warning(warning)
else:
    st.error(warning)

st.subheader("📊 Confidence")

st.write(f"{confidence}%")