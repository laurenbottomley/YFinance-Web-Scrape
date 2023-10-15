import yfinance as yf
import numpy as np
import pandas as pd

# Create a ticker object for the S&P 500
sp500 = yf.Ticker("^GSPC")

# Get historical data
sp500_history = sp500.history(period="max")

# Calculate the mean daily return
daily_mean_returns = np.mean(sp500_history['Close'].pct_change())

# Calculate the monthly returns
sp500_monthly = sp500_history['Close'].resample('M').last()
monthly_returns = sp500_monthly.pct_change()
mean_monthly_return = monthly_returns.mean()

# Approximate number of trading days in a year
trading_days_per_year = 252

# Calculate the annualized return
annual_mean_returns = daily_mean_returns * trading_days_per_year

# Create a DataFrame to store the results
results = pd.DataFrame({
    "Daily Mean Returns": [daily_mean_returns],
    "Mean Monthly Returns": [mean_monthly_return],
    "Annualized Mean Returns": [annual_mean_returns]
})

results.to_csv('data/sp500_returns.csv', index=False)
results.to_excel('data/sp500_returns.xlsx', index=False)

print(f"Daily Mean Returns: {daily_mean_returns:.6f}")
print(f"Mean Monthly Returns: {mean_monthly_return:.6f}")
print(f"Annualized Mean Returns: {annual_mean_returns:.2%}")
