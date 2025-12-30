def moving_average(prices, window=7):
    if len(prices) < window:
        return None
    return sum(prices[-window:]) / window
