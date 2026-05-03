#Calculate measures of dispersion from CSV data using Pandas.
import pandas as pd

# Load dataset (no column names)
data = pd.read_csv("iris.csv")

# Select column (SepalWidth = column index 1)
col = data["sepal.width"]

# Variance
variance = col.var()

# Standard Deviation
std_dev = col.std()

# Range
data_range = col.max() - col.min()

# Output
print("Variance:", variance)
print("Standard Deviation:", std_dev)
print("Range:", data_range)