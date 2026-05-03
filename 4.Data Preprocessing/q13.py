#13. Convert categorical values into numeric using LabelEncoder or OneHotEncoder. 

import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("preprocessing.csv")
print(data.head())
le = LabelEncoder()

# Select all categorical columns
cat_cols = data.select_dtypes(include='object')

# Apply encoding to each column
for col in cat_cols:
    data[col] = le.fit_transform(data[col])

print("preprocess\n",data.head())


'''import pandas as pd

df = pd.read_csv("preprocessing.csv")

# Convert ALL categorical columns at once
df = pd.get_dummies(df)

print(df.head())'''