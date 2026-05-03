#Convert categorical values into numeric using Tennis dataset.
import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("tennis.csv")
print(df.head())
le = LabelEncoder()

# Select all categorical columns
cat_cols = df.select_dtypes(include='object')

# Apply encoding to each column
for col in cat_cols:
    df[col] = le.fit_transform(df[col])

print("preprocess\n",df.head())