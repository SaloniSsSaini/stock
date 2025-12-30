def get_trend(prices):
    if prices[-1] > prices[0]:
        return "Up 📈"
    elif prices[-1] < prices[0]:
        return "Down 📉"
    return "Flat ➖"
