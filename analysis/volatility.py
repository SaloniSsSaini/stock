import numpy as np

def get_volatility(prices):
    # Convert to clean 1D numpy array
    prices = np.array(prices, dtype=float).flatten()

    if len(prices) < 2:
        return 0.0

    returns = np.diff(prices) / prices[:-1]
    volatility = np.std(returns) * 100

    return round(float(volatility), 2)
