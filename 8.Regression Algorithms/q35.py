#35 Simple Linear Regression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("salary.csv")

# Features and target
x = data[['Experience']]
y = data['Salary']

# Split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Model
linear_model = LinearRegression()
linear_model.fit(x_train, y_train)

# Prediction
predicted_values = linear_model.predict(x_test)
print("Predicted Salary:\n", predicted_values)