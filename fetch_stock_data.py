import yfinance as yf
import pandas as pd

tickers = ["AAPL", "MSFT", "GOOGL", "TSLA", "AMZN"]
start_date = "2018-01-01"
end_date = "2025-07-29"
data = yf.download(tickers, start=start_date, end=end_date)
data.to_csv("StockPrices.csv")
print("Stock data saved to stock_prices.csv")
