#Write a Python program to identify outliers.
import pandas as pd

# Load data
data = pd.read_csv('iris.csv')

# Use column as-is (or rename for simplicity)
data.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "variety"]

# Select one column
col = data["sepal_length"]

# IQR calculation
Q1 = col.quantile(0.25)
Q3 = col.quantile(0.75)
IQR = Q3 - Q1

# Bounds
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# Outliers
outliers = col[(col < lower) | (col > upper)]

# Output
print("Outliers:\n", outliers)
print("Lower bound:", lower)
print("Upper bound:", upper)