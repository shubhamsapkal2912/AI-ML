'''#25. Perform pre-processing of Play Tennis dataset (handle missing values, encoding, 
normalization, train-test split). '''

# Perform preprocessing (missing values, encoding, normalization, split)

import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

# Load dataset
df = pd.read_csv("tennis.csv")
print(df.head())

# -------------------------------
# Handle Missing Values
# -------------------------------
imputer = SimpleImputer(strategy="most_frequent")
df = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

# -------------------------------
# Encoding
# -------------------------------
le = LabelEncoder()
cat_cols = df.select_dtypes(include='object')

for col in cat_cols:
    df[col] = le.fit_transform(df[col])

# -------------------------------
# Normalization
# -------------------------------
scaler = MinMaxScaler()
num_cols = df.select_dtypes(include='number')

for col in num_cols:
    df[col] = scaler.fit_transform(df[[col]])

print("\nPreprocessed Data:\n", df.head())

# -------------------------------
# Train-Test Split
# -------------------------------
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

print("Training:", x_train.shape)
print("Testing :", x_test.shape)