def williams_r(df, period=14):
    high = df["High"].rolling(period).max()
    low = df["Low"].rolling(period).min()
    return -100 * (high - df["Close"]) / (high - low)
