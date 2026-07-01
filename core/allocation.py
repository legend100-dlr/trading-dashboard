import numpy as np

def compute_weights(returns_df):
    mu = returns_df.mean()
    cov = returns_df.cov()

    inv_cov = np.linalg.inv(cov + np.eye(len(cov))*1e-5)
    weights = inv_cov @ mu

    weights = weights * 0.3
    weights = np.clip(weights, 0, 1)

    return weights / weights.sum()