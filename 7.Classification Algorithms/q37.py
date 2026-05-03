
#37 Implement Decision Tree classification using Play Tennis dataset. 

from sklearn.preprocessing  import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

#load dataset
df=pd.read_csv("PlayTennis.csv")

#convert categorail value into numerical value
le=LabelEncoder()
for col in df.columns:
    df[col]=le.fit_transform(df[col])

#Split
x=df.iloc[:,:-1]
y=df.iloc[:,-1]

x_train,x_test,y_train,y_test=train_test_split(x,y, test_size=0.2,random_state=42)

#model selection
model=DecisionTreeClassifier(max_depth=1)
model.fit(x_train,y_train)

#prediction
y_pred=model.predict(x_test)

print("accuracy score on tennis",accuracy_score(y_test,y_pred))

print("Precision:", precision_score(y_test, y_pred))
print("Recall   :", recall_score(y_test, y_pred))
print("F1 Score :", f1_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))