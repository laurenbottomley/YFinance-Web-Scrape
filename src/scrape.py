import requests
from bs4 import BeautifulSoup
import yfinance as yf
import pandas as pd


# Get the list of S&P 500 companies from Wikipedia
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
response = requests.get(url, timeout=30)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', {'class': 'wikitable'})
df = pd.read_html(str(table))[0]
tickers = df['Symbol'].tolist()

# Fetch stock data for each company
data = yf.download(tickers, start='2023-01-01', end='2023-12-31')

# Save the data to CSV and Excel
csv_file = data.to_csv('data/output.csv')
excel_file = data.to_excel('data/output.xlsx')