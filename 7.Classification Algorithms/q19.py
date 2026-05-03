#19. Implement Naive Bayes classifier using Play Tennis dataset.

import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

#Load dataset
data=pd.read_csv("tennis.csv")
print(data.head())

#convert categorial to numeric
label_encoder=LabelEncoder()
for col in data.columns:
    data[col]=label_encoder.fit_transform(data[col])

print(data.head())

#feature Selection
x=data.drop(columns=['Play Tennis'])
y=data['Play Tennis']

#train test split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

#model
model=GaussianNB()
model.fit(x_train,y_train)

#predict
y_pred=model.predict(x_test)

print("Accuracy : ",accuracy_score(y_test,y_pred))