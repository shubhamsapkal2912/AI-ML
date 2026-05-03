import pandas as pd

# Required imports
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = datasets.load_iris()

X = iris.data      # Features
y = iris.target    # Target variable

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Decision Tree model
decision_tree_classifier = DecisionTreeClassifier()

# Train model
decision_tree_classifier.fit(X_train, y_train)

# Predict
y_pred = decision_tree_classifier.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)