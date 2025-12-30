import numpy as np

def correlation(prices_a, prices_b):
    min_len = min(len(prices_a), len(prices_b))
    return round(
        np.corrcoef(prices_a[-min_len:], prices_b[-min_len:])[0, 1],
        2
    )
