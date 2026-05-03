import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
data=pd.read_csv("Mall_Customers.csv")

x=data[['Annual Income (k$)','Spending Score (1-100)']].values

model=AgglomerativeClustering(n_clusters=5)
y=model.fit_predict(x)

#Evaluate
score=silhouette_score(x,y)
print("Silhouette Score",score)

#Plotting
plt.scatter(x[:,0],x[:,1],c=y)
plt.title("Scatter Plot")
plt.ylabel("Spending Score (1-100)")
plt.xlabel("Annual Income (k$)")
plt.show()
 