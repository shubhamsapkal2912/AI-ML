#29 Visualize Frequency Distribution using Histogram
import pandas as pd
import matplotlib.pyplot as plt
# Load dataset
data = pd.read_csv("Mall_Customers.csv")
# Select column
age = data['Age']
# -------------------------------
# Histogram
# -------------------------------
plt.hist(age, bins=10)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()