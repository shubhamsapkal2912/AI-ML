#Write a Python program to visualize data distribution
import pandas as pd
import matplotlib.pyplot as plt
# Load dataset
df = pd.read_csv("Mall_Customers.csv")
# Histogram (Distribution)
plt.hist(df['Age'])
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
# Box Plot (Outliers + Spread)
plt.boxplot(df['Annual Income (k$)'])
plt.title("Income Distribution")
plt.show()