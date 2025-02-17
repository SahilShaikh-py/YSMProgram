import pandas as pd
import matplotlib.pyplot as plt

# Load Excel file
file_path = "data.xlsx"  # Replace with your Excel file name
sheet_name = "Sheet1"  # Change if needed

# Read the Excel file
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Assuming Excel has two columns: 'Category' and 'Value'
categories = df["Category"]  # Labels
values = df["Value"]  # Data for pie chart

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=140, colors=['blue', 'green', 'red', 'orange', 'purple'])

# Add a title
plt.title("Pie Chart from Excel Data")

# Show the chart
plt.show()
