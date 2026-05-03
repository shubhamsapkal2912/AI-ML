#32. Implement Decision Tree classifier using Iris dataset. 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,f1_score,confusion_matrix,precision_score

#load data
data=pd.read_csv("iris.csv")
print(data.head)

#feature selection
x=data.drop(columns=['target'])
y=data['target']

#train test split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

#model
model=DecisionTreeClassifier()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)
# print("Predicted Score : ",y_pred)

print("Accuracy : ",accuracy_score(y_test,y_pred))
print("F1 : ",f1_score(y_test,y_pred,average='micro'))
print("Confusion : \n",confusion_matrix(y_test,y_pred))
print("Precision : ",precision_score(y_test,y_pred,average='micro'))

