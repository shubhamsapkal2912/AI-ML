#Q27 Write a Python program to create a frequency distribution
import pandas as pd

# Load dataset
df = pd.read_csv("Mall_Customers.csv")

# -------------------------------
# 1. Simple Frequency
# -------------------------------
print("Spending Score Frequency:\n")
freq1 = df['Spending Score (1-100)'].value_counts().sort_index()
print(freq1)

# -------------------------------
# 2. Grouped Frequency (Age)
# -------------------------------
bins = [0, 20, 30, 40, 50, 60, 100]
age_group = pd.cut(df['Age'], bins)

print("\nAge Group Frequency:\n")
freq2 = age_group.value_counts()
print(freq2)