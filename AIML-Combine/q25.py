import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split

# Step 1: Create dataset (Play Tennis)
data = {
    'Outlook': ['Sunny','Sunny','Overcast','Rain','Rain','Rain','Overcast','Sunny','Sunny','Rain','Sunny','Overcast','Overcast','Rain'],
    'Temperature': ['Hot','Hot','Hot','Mild','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Mild','Hot','Mild'],
    'Humidity': ['High','High','High','High','Normal','Normal','High','High','Normal','Normal','Normal','High','Normal','High'],
    'Wind': ['Weak','Strong','Weak','Weak','Weak','Strong','Strong','Weak','Weak','Weak','Strong','Strong','Weak','Strong'],
    'PlayTennis': ['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']
}

df = pd.DataFrame(data)

# Step 2: Handle missing values (example: fill with mode)
df = df.fillna(df.mode().iloc[0])

# Step 3: Encoding (convert categorical to numeric)
le = LabelEncoder()
for col in df.columns:
    df[col] = le.fit_transform(df[col])

# Step 4: Split features and target
X = df.drop('PlayTennis', axis=1)
y = df['PlayTennis']

# Step 5: Normalization (scale values between 0 and 1)
scaler = MinMaxScaler()
X = scaler.fit_transform(X)

# Step 6: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Output
print("Training Data Size:", X_train.shape)
print("Testing Data Size:", X_test.shape)