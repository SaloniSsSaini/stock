import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Stock Pulse Pro")

    parser.add_argument(
        "tickers",
        nargs="+",
        help="Stock tickers (e.g. AAPL TSLA MSFT)"
    )

    parser.add_argument(
        "--period",
        default="30d",
        choices=["7d", "30d", "90d"],
        help="Time period for analysis"
    )

    return parser.parse_args()
