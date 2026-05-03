import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler
# Reading the CSV file
df = pd.read_csv('play_tennis.csv')
# Displaying the dataset before conversion
print("Dataset before converting categorical to numeric:")
print(df)
# Convert categorical to numeric using LabelEncoder
le = LabelEncoder()
df['outlook'] = le.fit_transform(df['outlook'])
df['temp'] = le.fit_transform(df['temp'])
df['humidity'] = le.fit_transform(df['humidity'])
df['wind'] = le.fit_transform(df['wind'])
df['play'] = le.fit_transform(df['play'])
print("\nAfter converting categorical to numeric:")
print(df)
