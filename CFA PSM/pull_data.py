# Import key librares and modules 
import pandas as pd
import numpy as np

# Import datetime module that comes pre-installed in Python 
# datetime offers classes that work with date & time information
import datetime as dt

import yfinance as yf
from ib_insync import IB

# Connect to Interactive Brokers
ib = IB()
ib.connect('127.0.0.1', 7496, clientId=1)

# Fetch portfolio data
portfolio = ib.portfolio()

# Disconnect from IB
ib.disconnect()

# Extract symbols from portfolio
# symbols = [position.contract.symbol for position in portfolio]
symbols = ['AAPL','TSLA','VOO','NVDA']

# Set the date range for the last 10 years
end_date = pd.Timestamp.today().date()
start_date = end_date - pd.DateOffset(years=10)

# Function to fetch historical data
def fetch_historical_data(symbol, start, end):
    stock = yf.Ticker(symbol)
    hist = stock.history(start=start, end=end)
    return hist['Close']

# Fetch historical close prices for each symbol
historical_data = {}
for symbol in symbols:
    historical_data[symbol] = fetch_historical_data(symbol, start_date, end_date)

# Combine the data into a single DataFrame
historical_df = pd.DataFrame(historical_data)

# Save the DataFrame to a CSV file
#historical_df.to_csv('portfolio_historical_close_prices.csv')