import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler

df = pd.read_csv('play_tennis.csv')

le = LabelEncoder()

df['outlook'] = le.fit_transform(df['outlook'])
df['temp'] = le.fit_transform(df['temp'])
df['humidity'] = le.fit_transform(df['humidity'])
df['wind'] = le.fit_transform(df['wind'])
df['play'] = le.fit_transform(df['play'])

# Separate features (X) and target (y)
x = df.drop(columns=['play']) # Independent variables or x=df.iloc[:, :-1]
y = df['play'] # Dependent variable or y = df.iloc[:, -1]

# Rescale values between 0 and 1 using MinMaxScaler
scaler = MinMaxScaler()

X_scaled = scaler.fit_transform(x)

# Displaying the scaled features
print("\nScaled features (MinMaxScaler):")

print(X_scaled)
# Alternatively, normalize data using StandardScaler
scaler_standard = StandardScaler()
X_standard_scaled = scaler_standard.fit_transform(x)
# Displaying the standardized features
print("\nStandardized features (StandardScaler):")
print(X_standard_scaled)
