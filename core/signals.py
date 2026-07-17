def compute_signal(df, vix):

    close = float(df["Close"].iloc[-1])
    ma50 = float(df["MA50"].iloc[-1])

    score = 0

    # Trend
    if close > ma50:
        score += 1
    else:
        score -= 1

    # Volatility
    if vix < 18:
        score += 1
    elif vix > 20:
        score -= 1

    if score >= 2:
        return {
            "portfolio_regime": "AGGRESSIVE RISK-ON",
            "bear_warning": "LOW RISK",
            "confidence": 90
        }

    elif score == 1:
        return {
            "portfolio_regime": "MODERATE RISK-ON",
            "bear_warning": "LOW RISK",
            "confidence": 75
        }

    elif score == 0:
        return {
            "portfolio_regime": "NEUTRAL",
            "bear_warning": "BUILDING RISK",
            "confidence": 60
        }

    elif score == -1:
        return {
            "portfolio_regime": "MODERATE DEFENSIVE",
            "bear_warning": "ELEVATED RISK",
            "confidence": 75
        }

    else:
        return {
            "portfolio_regime": "AGGRESSIVE DEFENSIVE",
            "bear_warning": "HIGH RISK",
            "confidence": 90
        }