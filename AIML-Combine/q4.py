#4

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score

# Load dataset
data = pd.read_csv("/Mall_Customers.xls")

# Select Annual Income and Spending Score
X = data.iloc[:, [3,4]].values

# Train-Test Split
X_train, X_test = train_test_split(X, test_size=0.2)

# Apply Agglomerative Clustering
model = AgglomerativeClustering(n_clusters=5)
y = model.fit_predict(X_train)

# Evaluate model
score = silhouette_score(X_train, y)
print("Silhouette Score:", score)

# Plot clusters
plt.scatter(X_train[:,0], X_train[:,1], c=y)
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")
plt.show()