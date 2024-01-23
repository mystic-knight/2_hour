import yfinance as yf
from datetime import datetime, timedelta

# Example stock symbol (you can replace it with any stock symbol of your choice)
stock_symbol = 'BSESN'

# Get stock price data
stock_data = yf.download(stock_symbol, start=datetime.now() - timedelta(days = 360), end=datetime.now(), actions = True)

# Get basic company information
company_info = yf.Ticker(stock_symbol).info

# Display the results
print(f"Stock Price Data for {stock_symbol}:")
print(stock_data)

print("\nBasic Company Information:")
for key, value in company_info.items():
    print(f"{key}: {value}")

