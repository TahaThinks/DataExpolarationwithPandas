import pandas as pd

df = pd.read_csv('sample_data/salaries_by_college_major.csv')
# print(df.head())

# Setting the max n rows and columns to be printed
# pd.options.display.max_columns = None
# pd.options.display.max_rows = None

# How many rows & columns does the dataframe have?
print(f"Number of Rows: {df.shape[0]}")
print(f"Number of Columns: {df.shape[1]}")

# What are the labels for the columns? Do the columns have names?
# [print(column) for column in df.columns]

# Are there any missing values in our dataframe? Does our dataframe contain any bad data?
# print(df.isna())

# Create new Data Frame without Null Values
clean_df = df.dropna()

# Find College Major with Highest Starting Salaries?
# Undergraduate Major
# Starting Median Salary
# Mid-Career Median Salary
# Mid-Career 10th Percentile Salary
# Mid-Career 90th Percentile Salary
# Group
highest_starting_salary = clean_df["Starting Median Salary"].max()
print(f"Highest Starting Salary: {highest_starting_salary}")

highest_starting_salary_row = clean_df["Starting Median Salary"].idxmax()
print(highest_starting_salary_row)