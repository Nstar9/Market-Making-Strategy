import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Download TSLA stock data (adjust time frame as needed)
def fetch_stock_data(ticker="TSLA", start="2020-01-01", end="2025-01-01", interval="1d"):
    print(f"📈 Fetching {ticker} data from {start} to {end}...")
    
    # Download historical data
    stock_data = yf.download(ticker, start=start, end=end, interval=interval)
    
    # Save data as CSV
    stock_data.to_csv(f"{ticker}_data.csv")
    
    print(f"✅ Data saved as {ticker}_data.csv")
    return stock_data

# Fetch Tesla data
tsla_data = fetch_stock_data()

# Plot the closing price
plt.figure(figsize=(12, 6))
plt.plot(tsla_data["Close"], label="TSLA Closing Price", color="blue")
plt.title("Tesla (TSLA) Stock Price Over Time")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.show()
