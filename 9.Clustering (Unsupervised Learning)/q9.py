'''#9. Case Study: Apply K-Means Clustering on Mall Customers dataset to identify profitable 
customer groups. '''

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_csv("Mall_Customers.csv")

x = data[['Annual Income (k$)', 'Spending Score (1-100)']]

# Apply K-Means
model = KMeans(n_clusters=5, random_state=42)
data['Cluster'] = model.fit_predict(x)

# Find Most Profitable Cluster
avg = data.groupby('Cluster')[['Annual Income (k$)', 'Spending Score (1-100)']].mean()
print("Cluster Averages:\n", avg)

best = (avg['Annual Income (k$)'] + avg['Spending Score (1-100)']).idxmax()
print("Most Profitable Cluster:", best)

# Graph
plt.scatter(x['Annual Income (k$)'], x['Spending Score (1-100)'], c=data['Cluster'])

# Highlight profitable group
p = data[data['Cluster'] == best]
plt.scatter(p['Annual Income (k$)'], p['Spending Score (1-100)'],s=100)

plt.title("Customer Segments")
plt.xlabel("Income")
plt.ylabel("Spending Score")
plt.show()

