import yfinance as yf

def fetch_close_prices(ticker, period):
    data = yf.download(ticker, period=period, progress=False)

    if data.empty:
        raise ValueError(f"No data for {ticker}")

    # ensure 1D list
    close_prices = data["Close"].values.flatten().tolist()
    return close_prices
