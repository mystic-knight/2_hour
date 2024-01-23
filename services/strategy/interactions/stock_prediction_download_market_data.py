
import yfinance as yf

# Ensure you have yfinance installed: pip install yfinance

# show data for different tickers
start_date = '2004-08-01'

# Validating the tickers before using them
tickers = ['ETH-USD', 'GOOG', 'FB', 'TSLA']

for stock in tickers:
    data = yf.download(stock, start=start_date, end='2024-01-23')
    print(f"\nStock: {stock}\n{data}")
