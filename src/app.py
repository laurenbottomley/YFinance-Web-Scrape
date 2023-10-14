import requests
from bs4 import BeautifulSoup
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt  # Import the pyplot module


# Get the list of S&P 500 companies from Wikipedia
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
response = requests.get(url, timeout=30)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', {'class': 'wikitable'})
df = pd.read_html(str(table))[0]
tickers = df['Symbol'].tolist()

# Fetch stock data for each company
data = yf.download(tickers, start='2023-01-01', end='2023-12-31')

# Data is now stored in the 'data' variable as a Pandas DataFrame
print(data.head())

# reroute outputs to be in data folder
csv_file = data.to_csv('data/output.csv')
excel_file = data.to_excel('data/output.xlsx')



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