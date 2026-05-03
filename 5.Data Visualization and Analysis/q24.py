# Write a Python program to perform Correlation Analysis
import pandas as pd
# Step 1: Load dataset
data = pd.read_csv("Car.csv")
# Step 2: Select numeric columns only
numeric_data = data.select_dtypes(include='number')
# -------------------------------
# Correlation Analysis
# -------------------------------
correlation = numeric_data.corr()
print("Correlation Matrix:\n")
print(correlation)

import matplotlib.pyplot as plt
import seaborn as sns

sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()