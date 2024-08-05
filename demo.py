import pandas as pd
import numpy as np

# Read the CSV data
file_path = pd.read_csv('C:/Users/ADMIN/PycharmProjects/demo/market_trend_table2.csv')

print(file_path)


missing_values = file_path.isnull().sum()
print(missing_values)


# Assuming TrendID should be unique, fill missing values with unique IDs
file_path['TrendID'] = file_path['TrendID'].fillna(pd.Series(range(1, len(file_path) + 1)))


cleaned_file_path = 'cleaned_market_trend_table2.csv'
file_path.to_csv(cleaned_file_path, index=False)


