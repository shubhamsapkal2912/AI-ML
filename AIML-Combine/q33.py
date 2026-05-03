# Importing necessary libraries
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
# Load the Iris dataset
iris = datasets.load_iris()
X = iris.data # Features
y = iris.target # Target variable
# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Creating SVM classifier
svm_classifier = SVC(kernel='linear') # Linear kernel
# Other options for the kernel parameter are 'poly', 'rbf', 'sigmoid', etc.
# Training the classifier
svm_classifier.fit(X_train, y_train)
# Making predictions on the testing set
y_pred = svm_classifier.predict(X_test)
# Calculating the accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
