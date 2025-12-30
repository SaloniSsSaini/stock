# Stock Pulse Pro

Stock Pulse Pro is a lightweight, command-line Python tool that analyzes real
stock market data using Yahoo Finance. It provides quick insights into stock
trends, volatility, and short-term price behavior directly in the terminal.

---

## Features
- Fetches real stock data using `yfinance`
- Calculates price trend (Up / Down / Flat)
- Measures volatility using daily returns
- Computes a short-term moving average
- Displays simple ASCII charts in the terminal
- Simulates a basic moving-average trading strategy

---

## Tech Stack
- Python 3
- yfinance
- pandas
- numpy

---

## How to Run
```bash
pip install -r requirements.txt
python main.py AAPL TSLA --period 7d

Project Structure
stock/
├── main.py
├── cli.py
├── data/
├── analysis/
├── visualization/
├── strategy/
├── tests/
├── requirements.txt
└── README.md

Notes

This project focuses on clean structure, real market data handling, and
practical analysis rather than UI-heavy dashboards.

Future Improvements

Portfolio analysis

Backtesting with transaction costs

Data caching
