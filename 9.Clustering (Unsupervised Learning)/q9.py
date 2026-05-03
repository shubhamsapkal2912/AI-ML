#9. Case Study: Apply K-Means Clustering on Mall Customers dataset to identify profitable customer groups.
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
# Load dataset
data = pd.read_csv("Mall_Customers.csv")
# Select features
X = data.iloc[:, [3, 4]].values
# Apply K-Means
kmeans = KMeans(n_clusters=5, random_state=42)
labels = kmeans.fit_predict(X)
# Add cluster labels
data['Cluster'] = labels
# Plot clusters
plt.scatter(X[:, 0], X[:, 1], c=labels)
# Plot centroids
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200)
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")
plt.show()
# Cluster analysis
print(data.groupby('Cluster')[['Annual Income (k$)', 'Spending Score (1-100)']].mean())