import ib_insync
import pandas as pd
from ib_insync import IB, util

# Initialize the IB instance
ib = IB()

# Connect to IB Gateway or TWS (localhost:7497 is the default paper trading port)
ib.connect("127.0.0.1", 7496, clientId=0)

# Fetch portfolio data
portfolio = ib.portfolio()

# Disconnect after retrieving data
ib.disconnect()

# Convert portfolio data to a pandas DataFrame
portfolio_data = [
    {
        'Contract': p.contract.symbol,
        'Quantity': p.position,
        'MarketPrice': p.marketPrice,
        'MarketValue': p.marketValue,
        'AverageCost': p.averageCost,
        'UnrealizedPNL': p.unrealizedPNL,
        'RealizedPNL': p.realizedPNL,
        'Account': p.account
    } for p in portfolio
]

df = pd.DataFrame(portfolio_data)

# Display the DataFrame
print(df)

