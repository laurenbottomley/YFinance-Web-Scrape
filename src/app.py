import pandas as pd

data = pd.read_excel('data/output.xlsx', header=1)

# Exclude the first column
data = data.iloc[:, 1:]

# Exclude the first three rows
data = data.iloc[3:]

# Calculate Z-scores for the remaining data
z_scores = data.apply(lambda x: (x - x.mean()) / x.std())

#print(z_scores)
# output to csv and excel
csv_file = z_scores.to_csv('data/z-scores.csv')
excel_file = z_scores.to_excel('data/z-scores.xlsx')
