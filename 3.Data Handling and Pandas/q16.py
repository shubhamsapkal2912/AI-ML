#Write a Python program to import CSV file and calculate measures of central tendency.
import pandas as pd

# Read CSV file
df = pd.read_csv("Mall_Customers.csv")

# Calculate measures
print("Mean:\n", df.mean(numeric_only=True))
print("\nMedian:\n", df.median(numeric_only=True))
print("\nMode:\n", df.mode(numeric_only=True))