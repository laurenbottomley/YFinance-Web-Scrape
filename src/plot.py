import matplotlib.pyplot as plt  # Import the pyplot module


# # Calculate daily returns


# daily_returns = data['Adj Close'].pct_change()

# # Plot the daily returns of a specific company (e.g., Apple)
# daily_returns['AAPL'].plot()
# plt.title('Daily Returns of Apple')
# plt.xlabel('Date')
# plt.ylabel('Returns')
# plt.show()

# mean_returns = daily_returns.mean()
# mean_returns.plot(kind='bar')
# plt.title('Average Daily Returns for S&P 500 Stocks')
# plt.xlabel('Stock Ticker')
# plt.ylabel('Average Daily Return')
# plt.show()