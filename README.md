# Stock Pulse Pro 📈

Stock Pulse Pro is an advanced, CLI-based Python project that analyzes real stock
market data using Yahoo Finance. The tool provides insights such as stock trends,
volatility, moving averages, terminal-based charts, and even simulates a simple
trading strategy.

The goal of this project is to demonstrate clear thinking, clean architecture,
and practical data analysis rather than heavy UI or overengineering.

---

## 🚀 Features

### Core Functionality
- Fetches real stock market data using `yfinance`
- Calculates stock **trend** (Up / Down / Flat)
- Measures **volatility** using daily returns
- Computes **7-day moving average**

### Advanced Analysis
- Ranks stocks by volatility
- Displays **ASCII price charts** directly in the terminal
- Calculates correlation between stocks
- Simulates a **moving-average based trading strategy**

### CLI Support
- Accepts multiple stock tickers
- Configurable analysis period (`7d`, `30d`, `90d`)
- Clean and readable terminal output

---

## 🧠 Why I Built This Project

I wanted to build a lightweight, terminal-first stock analysis tool that focuses
on extracting meaningful insights from market data without relying on dashboards
or complex visual interfaces. This project helped me explore how data fetching,
analysis, visualization, and strategy simulation can be structured cleanly in
Python.

---

## 🗂 Project Structure

stock-pulse/
│
├── main.py # Application entry point
├── cli.py # Command-line argument parsing
│
├── data/
│ └── fetcher.py # Yahoo Finance data fetching
│
├── analysis/
│ ├── trend.py # Trend detection logic
│ ├── volatility.py # Volatility calculation
│ ├── moving_average.py # Moving average calculation
│ └── correlation.py # Stock correlation analysis
│
├── visualization/
│ └── ascii_chart.py # Terminal-based ASCII charts
│
├── strategy/
│ └── ma_strategy.py # Moving average trading strategy
│
├── tests/
│ └── test_analysis.py # Unit tests for core logic
│
├── requirements.txt
└── README.md

yaml
Copy code

---

## ⚙️ How to Run

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
2️⃣ Run the Program
bash
Copy code
python main.py AAPL TSLA MSFT --period 30d
Example Output
yaml
Copy code
📊 Stock Pulse Pro Report

AAPL
  Trend: Up 📈
  Volatility: 1.34%
  7-day MA: 192.12
  Chart: ▁▂▃▄▅▆▇█
  Strategy → Trades: 6, P/L: ₹820.5
----------------------------------------
🔥 Most Volatile Stock: TSLA (3.98%)
🧪 Tests
Basic unit tests are included for core logic such as trend detection.

Run tests using:

bash
Copy code
pytest
🧩 Design Decisions
Chose a CLI-first approach to keep the tool fast and lightweight

Separated data fetching, analysis, visualization, and strategy logic

Used simple and explainable financial calculations

Avoided heavy UI frameworks to focus on core data handling

⚖️ Trade-offs
Yahoo Finance is free but may have rate limits

Trading strategy ignores transaction costs for simplicity

Volatility calculation is intentionally simplified for clarity

🔮 Future Improvements
Portfolio-level analysis

Backtesting with transaction costs

Exporting results to CSV

Web dashboard using FastAPI

Caching API responses

