import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data\Superstore Sales Dataset.csv")

# Show first 5 rows
print(df.head())

# Remove empty values
df.dropna(inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Save cleaned file
df.to_csv("data/cleaned_data.csv", index=False)

print("Data Cleaned Successfully")

# Sales chart
df.groupby('Category')['Sales'].sum().plot(kind='bar')

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.show() 
