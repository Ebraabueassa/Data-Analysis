import pandas as pd
import matplotlib.pyplot as plt

# Manually input stock prices
data = {
    "Date": ["2024-02-20", "2024-02-21", "2024-02-22", "2024-02-23", "2024-02-24"],
    "TSLA": [200, 205, 210, 208, 215],
    "QQQ": [350, 352, 348, 355, 360],
    "PLTR": [15, 16, 17, 16.5, 18],
    "NVDA": [500, 510, 505, 515, 520],
    "ARKK": [45, 46, 47, 46.5, 48],
    "SPY": [420, 422, 419, 425, 430]
}

# Convert to DataFrame
prices = pd.DataFrame(data)
prices["Date"] = pd.to_datetime(prices["Date"])
prices.set_index("Date", inplace=True)

# Calculate daily price changes using subtraction
previous_prices = prices.shift(1).fillna(prices)
daily_changes = prices - previous_prices

# Plot daily changes
plt.figure(figsize=(12, 6))
for ticker in daily_changes.columns:
    plt.plot(daily_changes.index, daily_changes[ticker], label=ticker)

plt.legend()
plt.title("Daily Price Changes of Stocks")
plt.xlabel("Date")
plt.ylabel("Price Change")
plt.grid()
plt.show()
