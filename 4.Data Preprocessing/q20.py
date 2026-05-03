#20. Write a Python program to split dataset into training and testing dataset. 

from sklearn.model_selection import train_test_split
import pandas as pd
df=pd.read_csv("Mall_Customers.csv")

x=df[['Age','Annual Income (k$)']]
y=df['Spending Score (1-100)']

x_train,x_test,y_train,y_test=train_test_split(x,y, test_size=0.2,random_state=42)
print("training data",x_train.shape)
print("testing data",x_test.shape)