# Step 1: Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Read the CSV file
df = pd.read_csv('C:/Users/ADMIN/PycharmProjects/demo/sales_data (1).csv')

# Step 3: Convert SaleDate to datetime
df['SaleDate'] = pd.to_datetime(df['SaleDate'])

# Step 4: Group by SaleDate and sum the Quantity
daily_sales = df.groupby('SaleDate')['Quantity'].sum().reset_index()

# Step 5: Sort by date
daily_sales = daily_sales.sort_values('SaleDate')

# Step 6: Create the line chart
plt.figure(figsize=(12, 6))
plt.plot(daily_sales['SaleDate'], daily_sales['Quantity'])

# Step 7: Customize the chart
plt.title('Daily Sales Quantity', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Total Quantity Sold', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(True, linestyle='--', alpha=0.7)

# Step 8: Format y-axis to show whole numbers
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x):,}'))

# Step 9: Adjust layout and display the plot
plt.tight_layout()
plt.show()