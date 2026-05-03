#33. Perform Support Vector Machine (SVM) classification using Iris dataset. 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

# Load data
df = pd.read_csv("iris.csv")

# Split
x = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Scaling using loop
scaler = StandardScaler()
for col in x.columns:
    x[col] = scaler.fit_transform(x[[col]])

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=42
)

# Model
model = SVC(kernel="linear")
model.fit(x_train, y_train)

# Predict
y_pred = model.predict(x_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))