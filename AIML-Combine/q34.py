# Importing necessary libraries
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = datasets.load_iris()

X = iris.data      # Features
y = iris.target    # Target variable

# Splitting dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Naive Bayes model
naive_bayes_classifier = GaussianNB()

# Train model
naive_bayes_classifier.fit(X_train, y_train)

# Predict
y_pred = naive_bayes_classifier.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)