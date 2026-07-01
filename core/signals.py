def compute_signal(df, vix):

    close = df["Close"].iloc[-1].item()
    ma50 = df["MA50"].iloc[-1].item()

    score = 0

    if close < ma50:
        score += 1

    if vix > 20:
        score += 1

    if score >= 2:
        return "RISK_OFF"
    return "RISK_ON"