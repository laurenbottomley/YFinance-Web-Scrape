import pandas as pd
import matplotlib.pyplot as plt

# Load your data
data = pd.read_excel('data/output.xlsx', header=1, index_col=0)

# Calculate the quartiles and IQR
Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3 - Q1

# Define lower and upper bounds
LB = Q1 - 1.5 * IQR
UB = Q3 + 1.5 * IQR

# Detect lower and upper outliers
lower_outliers = data < LB
upper_outliers = data > UB

# Combine the two outlier dataframes
outliers = lower_outliers | upper_outliers

# Print the count of outliers for each stock
outlier_counts = outliers.sum()

# Save the outlier counts to a CSV file
outlier_counts.to_csv('data/IQR_outlier_counts.csv')
outlier_counts.to_excel('data/IQR_outlier_counts.xlsx')

# Identify the stocks with the most outliers
stocks_with_most_outliers = outlier_counts.sort_values(ascending=False).head(20)

# Print the stocks with the most outliers
print("\nStock with the Most Outliers:")
print(stocks_with_most_outliers)

# create a bar chart of the outlier counts
plt.figure(figsize=(8, 6))
plt.bar(stocks_with_most_outliers.index, stocks_with_most_outliers.values)
plt.title('Stocks with the Most Outliers')
plt.xlabel('Stock Ticker')
plt.ylabel('Number of Outliers')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

