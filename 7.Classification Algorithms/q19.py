#19. Implement Naive Bayes classifier using Play Tennis dataset.
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("tennis.csv")

# Convert categorical to numeric
for col in df.columns:
    df[col] = LabelEncoder().fit_transform(df[col])

# Split data
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = GaussianNB()
model.fit(x_train, y_train)

# Prediction
y_pred = model.predict(x_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))