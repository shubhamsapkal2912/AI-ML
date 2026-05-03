import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Dataset
X = np.array([
    [130,110,2500],
    [150,130,2700],
    [200,150,3000],
    [120,95,2400],
    [180,160,3200],
    [140,120,2600],
    [250,190,3500],
    [300,210,4000],
    [230,180,3300],
    [160,140,2800]
])

y = np.array([15000,18000,25000,14000,22000,16000,28000,35000,27000,19000])

# Polynomial Features
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Model
model = LinearRegression()
model.fit(X_poly, y)

# Prediction (example)
pred = model.predict(poly.transform([[200,150,3000]]))
print("Predicted Car Price:", pred[0])