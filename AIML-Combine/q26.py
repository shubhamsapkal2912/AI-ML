import pandas as pd

data = pd.read_csv('iris.csv')
data.columns = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']

mean = data['SepalLength'].mean()
median = data['SepalLength'].median()
mode = data['SepalLength'].mode()[0]

print(f"Mean: {mean}, Median: {median}, Mode: {mode}")