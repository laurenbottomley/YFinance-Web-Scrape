import pandas as pd
import numpy as np

data = pd.read_excel('data/z-scores.xlsx', index_col=0)

# Set a threshold for outlier detection (e.g., z > 3 or z < -3)
outlier_threshold = 3

# Detect outliers based on z-scores
outliers = (np.abs(data) > outlier_threshold)

# Create a DataFrame of boolean values indicating outliers
outliers_df = pd.DataFrame(outliers, columns=data.columns)

# Print the count of outliers for each stock
outlier_counts = outliers_df.sum()

# Identify the stocks with the most outliers
stocks_with_most_outliers = outlier_counts.sort_values(ascending=False).head(20)

outlier_counts.to_csv('data/Z_outlier_counts.csv')
outlier_counts.to_excel('data/Z_outlier_counts.xlsx')

print("\nStock with the Most Outliers:")
print(stocks_with_most_outliers)

