# Import necessary libraries
import pandas as pd

# Create a sample dataset (or you can use pd.read_csv('file.csv'))
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 28],
    'Salary': [50000, 60000, 70000, 80000, 65000]
}

df = pd.DataFrame(data)

# Display first 5 rows
print("Head:\n", df.head())

# Display last 5 rows
print("\nTail:\n", df.tail())

# Display shape (rows, columns)
print("\nShape:", df.shape)

# Display information about DataFrame
print("\nInfo:")
df.info()

# Display statistical summary
print("\nDescribe:\n", df.describe())

# Display column names
print("\nColumns:", df.columns)