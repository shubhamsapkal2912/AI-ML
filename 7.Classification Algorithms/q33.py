#33. Perform Support Vector Machine (SVM) classification using Iris dataset. 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

#load data
data=pd.read_csv("iris.csv")
print(data.head())

# Feature Selection BEFORE scaling
x = data.drop(columns=['target'])
y = data['target']

# scale only features
scaler = StandardScaler()
x = scaler.fit_transform(x)

#split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
#model
model=SVC(kernel='linear')
model.fit(x_train,y_train)

y_pred=model.predict(x_test)
print("Accuracy : ",accuracy_score(y_test,y_pred))
