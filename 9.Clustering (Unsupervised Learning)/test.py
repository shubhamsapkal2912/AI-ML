import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv("Mall_Customers.csv")

x = df.iloc[:, [3, 4]].values

model = KMeans(n_clusters=5, random_state=42)
y = model.fit_predict(x)

df['Cluster'] = y

# Find most profitable cluster
avg = df.groupby('Cluster')[['Annual Income (k$)', 'Spending Score (1-100)']].mean()
best = (avg['Annual Income (k$)'] + avg['Spending Score (1-100)']).idxmax()

print("Most Profitable Cluster:", best)

# Plot
plt.scatter(x[:, 0], x[:, 1], c=y)

centroids = model.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1], s=200)

# Highlight best cluster
p = df[df['Cluster'] == best]
plt.scatter(p['Annual Income (k$)'], p['Spending Score (1-100)'], s=100)

plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")

plt.show() 