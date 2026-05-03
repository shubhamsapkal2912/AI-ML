import pandas as pd

# Load properly
data = pd.read_csv('iris.csv')

# Rename columns
data.columns = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']

# IQR method
Q1 = data['SepalLength'].quantile(0.25)
Q3 = data['SepalLength'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = data[(data['SepalLength'] < lower_bound) | 
                (data['SepalLength'] > upper_bound)]

print(outliers)
print("Q1:", Q1)
print("Q3:", Q3)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)
print("Min value:", data['SepalLength'].min())
print("Max value:", data['SepalLength'].max())