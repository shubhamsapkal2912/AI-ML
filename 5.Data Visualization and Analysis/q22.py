#Write a Python program to visualize data distribution
import pandas as pd
import matplotlib.pyplot as plt
# Load dataset
data = pd.read_csv("Mall_Customers.csv")
# Histogram (Distribution)
age=data['Age']
plt.hist(age)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
# Box Plot (Outliers + Spread)
annual_income=data['Annual Income (k$)']
plt.boxplot(annual_income)
plt.title("Income Distribution")
plt.show()