import pandas as pd

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
print("Number of Outliers for Each Stock:")
print(outlier_counts)

# Save the outlier counts to a CSV file
outlier_counts.to_csv('data/IQR_outlier_counts.csv')
outlier_counts.to_excel('data/IQR_outlier_counts.xlsx')