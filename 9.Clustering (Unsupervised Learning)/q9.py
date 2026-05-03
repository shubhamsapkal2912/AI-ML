#9. Case Study: Apply K-Means Clustering on Mall Customers dataset to identify profitable customer groups.
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#load Dataset
data=pd.read_csv("Mall_Customers.csv")

#Select the columns
x=data[['Annual Income (k$)','Spending Score (1-100)']].values

#Load the model
model=KMeans(n_clusters=5,random_state=42)
labels=model.fit_predict(x)

#add the cluster lables
data['Cluster']=labels

# plot the cluster
plt.scatter(x[:,0],x[:,1] ,c=labels)

#plot the centroid
centroid=model.cluster_centers_
plt.scatter(centroid[:,0],centroid[:,1],c='red')
plt.title("Profitable Customer")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.show()

# Cluster analysis
print(data.groupby('Cluster')[['Annual Income (k$)', 'Spending Score (1-100)']].mean())