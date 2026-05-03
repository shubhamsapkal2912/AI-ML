#14. Write a Python program to implement Data Normalization / Standardization. 

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

data = pd.read_csv("preprocessing.csv")

# Select numeric data
num = data.select_dtypes(include=['number'])

# Normalization
minmax = MinMaxScaler()
norm = minmax.fit_transform(num)

print("Normalized Data:\n", norm)

# Standardization (mean=0, std=1)
std = StandardScaler()
scaled = std.fit_transform(num)
print("\nStandardized Data:\n", scaled)