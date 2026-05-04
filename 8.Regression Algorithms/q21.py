#21 Apply Polynomial Regression to predict car price.
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#Load the dataset
data=pd.read_csv("Car.csv")

#Feature Selection
x=data[['Volume','Weight','CO2']]
y=data[['Price']]

#Polynomial Transformation
model_poly=PolynomialFeatures(degree=2)
x_poly=model_poly.fit_transform(x)

#Dataset Splitting
x_train,x_test,y_train,y_test=train_test_split(x_poly,y,test_size=0.2,random_state=42)

#model
linear_model=LinearRegression()
linear_model.fit(x_train,y_train)

predicted_values=linear_model.predict(x_test)
model_score=linear_model.score(x_test,y_test)

print("Predicted Values \n",predicted_values)
print("Model Score \n",model_score)




