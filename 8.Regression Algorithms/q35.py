#35 Simple Linear Regression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# Load dataset
df = pd.read_csv("salary.csv")
# Features and target
X = df[['Experience']]
y = df['Salary']
# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# Model
model = LinearRegression()
model.fit(X_train, y_train)
# Prediction
y_pred = model.predict(X_test)
print("Predicted Salary:\n", y_pred)