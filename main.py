import pandas as pd
import os




file_path = '/home/gautam/airflow/Fortune 2020.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)



df['no_of_employees'] = pd.to_numeric(df['no_of_employees'].str.replace(',', ''), errors='coerce')
df['revenues'] = pd.to_numeric(df['revenues'].str.replace(',', ''), errors='coerce')
df['revenue_change'] = pd.to_numeric(df['revenue_change'], errors='coerce')
df['profits'] = pd.to_numeric(df['profits'].str.replace(',', ''), errors='coerce')
df['profit_change'] = pd.to_numeric(df['profit_change'], errors='coerce')
df['assets'] = pd.to_numeric(df['assets'].str.replace(',', ''), errors='coerce')
df['market_value'] = pd.to_numeric(df['market_value'].str.replace(',', ''), errors='coerce')


# Inspect the first few rows
# print(df.head())

# Display summary information about the dataset
# print(df.info())

# Example filtering: Companies with more than 100,000 employees
# filtered_df1 = df[df['no_of_employees'] > 100000]
# print(filtered_df1.head())

# Example filtering: Companies with positive revenue change
# filtered_df2 = df[df['revenue_change'] > 0]
# print(filtered_df2.head())

# Example filtering: Companies with profits greater than $10,000
# filtered_df3 = df[df['profits'] > 10000]
# print(filtered_df3.head())

# Example filtering: Companies with more than 100,000 employees and positive revenue change
filtered_df = df[(df['no_of_employees'] > 100000) & ((df['profits'] > 80000) | (df['assets'] > 100000))]
print(filtered_df)

# filtered_df.to_csv(r'C:\Users\gauta\OneDrive\Desktop\apache project\filtered_data.csv', index=False)

output_file_path = '/home/gautam/airflow/filtered_data.csv'

# Save the filtered DataFrame to a CSV file in the same directory
filtered_df.to_csv(output_file_path, index=False)