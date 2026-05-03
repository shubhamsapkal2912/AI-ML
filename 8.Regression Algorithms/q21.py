#21
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
# Load dataset
df = pd.read_csv("Car.csv")
# Features and target
X = df[['Year']]
y = df['Price']
# Polynomial transformation
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.2, random_state=42)
# Model
model = LinearRegression()
model.fit(x_train, y_train)
# Prediction
y_pred = model.predict(x_test)
# Output
print("Predicted values:\n", y_pred)
print("Model Score:", model.score(x_test, y_test))