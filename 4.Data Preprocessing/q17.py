#Convert categorical values into numeric using Tennis dataset.
import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("tennis.csv")
print(data.head())
le = LabelEncoder()

# Select all categorical columns
cat_cols = data.select_dtypes(include='object')

# Apply encoding to each column
for col in cat_cols:
    data[col] = le.fit_transform(data[col])

print("preprocess\n",data.head())