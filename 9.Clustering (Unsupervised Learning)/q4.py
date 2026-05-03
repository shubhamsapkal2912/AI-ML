#4. Case Study: Identify profitable customer groups using Agglomerative Clustering on Spending Score dataset.
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
# Load dataset
data = pd.read_csv("Mall_Customers.csv")
# Select Annual Income and Spending Score
X = data.iloc[:, [3, 4]].values
# Apply Agglomerative Clustering
model = AgglomerativeClustering(n_clusters=5)
y = model.fit_predict(X)
# Evaluate model
score = silhouette_score(X, y)
print("Silhouette Score:", score)
# Plot clusters
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")
plt.show()