import yfinance as yf

def load_asset(ticker):
    df = yf.download(ticker, period="6mo")
    df["returns"] = df["Close"].pct_change()
    df["MA50"] = df["Close"].rolling(50).mean()
    return df