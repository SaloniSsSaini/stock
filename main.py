from cli import parse_args
from data.fetcher import fetch_close_prices
from analysis.trend import get_trend
from analysis.volatility import get_volatility
from analysis.moving_average import moving_average
from visualization.ascii_chart import ascii_chart
from strategy.ma_strategy import simulate_strategy

def main():
    args = parse_args()

    results = []

    print("\n📊 Stock Pulse Pro Report\n")

    for ticker in args.tickers:
        prices = fetch_close_prices(ticker, args.period)

        trend = get_trend(prices)
        vol = get_volatility(prices)
        ma = moving_average(prices)
        chart = ascii_chart(prices)
        trades, pnl = simulate_strategy(prices)

        results.append((ticker, vol))

        print(f"{ticker}")
        print(f"  Trend: {trend}")
        print(f"  Volatility: {vol}%")
        print(f"  7-day MA: {round(ma,2) if ma else 'N/A'}")
        print(f"  Chart: {chart}")
        print(f"  Strategy → Trades: {trades}, P/L: ₹{pnl}")
        print("-" * 40)

    most_volatile = max(results, key=lambda x: x[1])
    print(f"🔥 Most Volatile Stock: {most_volatile[0]} ({most_volatile[1]}%)")

if __name__ == "__main__":
    main()
