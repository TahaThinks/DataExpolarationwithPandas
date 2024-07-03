import pandas as pd

df = pd.read_csv('sample_data/salaries_by_college_major.csv')
# print(df.head())

# How many rows & columns does the dataframe have?
print(f"Number of Rows: {df.shape[0]}")
print(f"Number of Columns: {df.shape[1]}")
