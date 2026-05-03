import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

# Create sample dataset
data = {
    'Years_of_Experience': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Age': [22, 23, 25, 26, 28, 30, 32, 34, 36, 40],
    'Performance': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
    'Salary': [45000, 48000, 51000, 54000, 57000, 60000, 63000, 66000, 69000, 72000]
}

# Convert to DataFrame
df = pd.DataFrame(data)

print("Sample Data:")
print(df)

# Features (multiple inputs)
X = df[['Years_of_Experience', 'Age', 'Performance']]

# Target
y = df['Salary']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Standardize (optional but fine)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
print(f"\nMean Squared Error: {mse:.2f}")

# Model parameters
print(f"\nCoefficients: {model.coef_}")
print(f"Intercept: {model.intercept_}")

# Predict new data
new_data = [[5, 29, 72]]
new_data_scaled = scaler.transform(new_data)

predicted_salary = model.predict(new_data_scaled)
print(f"\nPredicted Salary: {predicted_salary[0]:.2f}")