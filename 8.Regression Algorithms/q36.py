#36 Multiple Linear Regression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# Load dataset
data = pd.read_csv("salary.csv")
# Features and target
x = data[['Experience', 'Age', 'Performance']]
y = data['Salary']
# Split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
# Model
model_linear = LinearRegression()
model_linear.fit(x_train, y_train)
# Prediction
y_pred = model_linear.predict(x_test)
print("Predicted Salary:\n", y_pred)