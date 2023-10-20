import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats


data = pd.read_excel('data/output.xlsx', header=1, index_col=0)

column_name = data.columns[0]

quantiles, _ = stats.probplot(data[column_name], dist="norm")

# Calculate mean and standard deviation of the data
mean = data[column_name].mean()
std = data[column_name].std()

# Create a Q-Q plot
plt.figure(figsize=(8, 6))
plt.scatter(quantiles[0], data[column_name].sort_values())
plt.title('Q-Q Plot for Distribution of Stock Prices')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Sample Quantiles')
plt.grid(True)

# Add a reference line
plt.plot([quantiles[0][0], quantiles[0][-1]], [mean - std, mean + std], color='red', linestyle='--')

# Show the Q-Q plot
plt.show()
