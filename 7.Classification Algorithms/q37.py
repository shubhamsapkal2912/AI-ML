#37 Implement Decision Tree classification using Play Tennis dataset. 

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,recall_score,f1_score,precision_score,confusion_matrix
from sklearn.tree import DecisionTreeClassifier

#load dataset
data=pd.read_csv("tennis.csv")
print(data.head())

#encode data
le=LabelEncoder()
columns=data.select_dtypes(include='object')
for col in columns:
    data[col]=le.fit_transform(data[col])
print(data.head())    

#select features
x=data.drop(columns=['Play Tennis'])
y=data['Play Tennis']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

model=DecisionTreeClassifier(max_depth=1)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)

print("Accuracy",accuracy_score(y_test,y_pred))
print("Recall Score",recall_score(y_test,y_pred))
print("F1 Score",f1_score(y_test,y_pred))
print("Precision Score",precision_score(y_test,y_pred))
print("Confusion Matrix",confusion_matrix(y_test,y_pred))




