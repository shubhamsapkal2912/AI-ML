#29 Visualize Frequency Distribution using Histogram
import pandas as pd
import matplotlib.pyplot as plt
# Load dataset
df = pd.read_csv("Mall_Customers.csv")
# Select column
data = df['Age']
# -------------------------------
# Histogram
# -------------------------------
plt.hist(data, bins=10)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()