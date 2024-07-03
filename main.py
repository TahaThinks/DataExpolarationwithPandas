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
# highest_starting_salary = clean_df["Starting Median Salary"].max()
# print(f"Highest Starting Salary: {highest_starting_salary}")
#
# highest_starting_salary_row = clean_df["Starting Median Salary"].idxmax()
# print(highest_starting_salary_row)
#
# highest_starting_salary_major = clean_df["Undergraduate Major"].loc[highest_starting_salary_row]
# print(highest_starting_salary_major)
#
# print(clean_df.loc[43])
#

# What college major has the highest mid-career salary?
highest_mid_career_salary_id = clean_df["Mid-Career Median Salary"].idxmax()
print(clean_df["Undergraduate Major"].loc[highest_mid_career_salary_id])
# How much do graduates with this major earn? (Mid-career is defined as having 10+ years of experience).
print(clean_df["Mid-Career Median Salary"].loc[highest_mid_career_salary_id])


# Which college major has the lowest starting salary and
lowest_starting_career_salary_id = clean_df["Starting Median Salary"].idxmin()
print(clean_df["Undergraduate Major"].loc[lowest_starting_career_salary_id])
# how much do graduates earn after university?
print(clean_df["Mid-Career Median Salary"].loc[lowest_starting_career_salary_id])
# Which college major has the lowest mid-career salary and
# how much can people expect to earn with this degree?
lowest_mid_career_salary_id = clean_df["Mid-Career Median Salary"].idxmin()
print(clean_df["Undergraduate Major"].loc[lowest_mid_career_salary_id])
print(clean_df["Starting Median Salary"].loc[lowest_mid_career_salary_id])
print(clean_df["Mid-Career Median Salary"].loc[lowest_mid_career_salary_id])
print(clean_df["Mid-Career 10th Percentile Salary"].loc[lowest_mid_career_salary_id])
print(clean_df["Mid-Career 90th Percentile Salary"].loc[lowest_mid_career_salary_id])


#Get Spread of Mid-Career 10th Percentile Salary & Mid-Career 90th Percentile Salary:
spread_col = clean_df["Mid-Career 90th Percentile Salary"] - clean_df["Mid-Career 10th Percentile Salary"]
clean_df.insert(1,"Spread",spread_col)
print(clean_df.head())
