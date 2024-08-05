import pandas as pd
import matplotlib.pyplot as plt

file_path = 'C:/Users/ADMIN/Downloads/web_access_category_table.csv'
data = pd.read_csv(file_path)

# Plotting Access Frequency by Category
plt.figure(figsize=(10, 6))
plt.bar(data['CategoryName'], data['AccessFrequency'], color='skyblue')
plt.xlabel('Category Name')
plt.ylabel('Access Frequency')
plt.title('Access Frequency by Category')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()



# Ensure the pie chart does not repeat data
# Create a pie chart to visualize the proportion of access frequencies for the first 20 unique categories
top_20_unique_data = data.drop_duplicates(subset='CategoryName').head(20)

plt.figure(figsize=(10, 6))
plt.pie(top_20_unique_data['AccessFrequency'], labels=top_20_unique_data['CategoryName'], autopct='%1.1f%%', startangle=140)
plt.title('Proportion of Access Frequency by Category (Top 20 Unique)')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.




# Create a scatter plot to visualize the relationship between Access Frequency and Average Session Duration
plt.figure(figsize=(10, 6))
plt.scatter(data['AccessFrequency'], data['AverageSessionDuration'], color='purple')
plt.xlabel('Access Frequency')
plt.ylabel('Average Session Duration')
plt.title('Access Frequency vs. Average Session Duration')
plt.grid(True)

# Table Display
plt.show()


