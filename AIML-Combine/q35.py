import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Create sample dataset
data = {
    'Years_of_Experience': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Salary': [45000, 48000, 51000, 54000, 57000, 60000, 63000, 66000, 69000, 72000]
}

# Convert to DataFrame
df = pd.DataFrame(data)

print("Sample Data:")
print(df)

# Features (independent variable)
X = df[['Years_of_Experience']]

# Target (dependent variable)
y = df['Salary']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
print(f"\nMean Squared Error: {mse:.2f}")

# Print model parameters
print(f"\nCoefficient (Slope): {model.coef_[0]}")
print(f"Intercept: {model.intercept_}")

# Predict new value
new_data = [[6]]
predicted_salary = model.predict(new_data)

print(f"\nPredicted salary for 6 years of experience: {predicted_salary[0]:.2f}")