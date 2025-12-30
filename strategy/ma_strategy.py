from analysis.moving_average import moving_average

def simulate_strategy(prices):
    cash = 0
    holding = False
    trades = 0

    for i in range(7, len(prices)):
        ma = sum(prices[i-7:i]) / 7
        price = prices[i]

        if price > ma and not holding:
            holding = True
            buy_price = price
            trades += 1

        elif price < ma and holding:
            holding = False
            cash += price - buy_price

    return trades, round(cash, 2)
