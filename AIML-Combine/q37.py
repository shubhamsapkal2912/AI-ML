import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Dataset
data = {
    'Outlook': ['Sunny','Sunny','Overcast','Rain','Rain','Rain','Overcast','Sunny'],
    'Temp': ['Hot','Hot','Hot','Mild','Cool','Cool','Mild','Hot'],
    'Humidity': ['High','High','High','High','Normal','Normal','Normal','High'],
    'Wind': ['Weak','Strong','Weak','Weak','Weak','Strong','Strong','Weak'],
    'Play': ['No','No','Yes','Yes','Yes','No','Yes','No']
}

df = pd.DataFrame(data)

# Encoding
le = LabelEncoder()
for col in df.columns:
    df[col] = le.fit_transform(df[col])

# Split features & target
X = df.drop('Play', axis=1)
y = df['Play']

# Model
model = DecisionTreeClassifier()
model.fit(X, y)

# Prediction (example input)
prediction = model.predict([[0, 2, 1, 0]])

print("Prediction:", prediction)