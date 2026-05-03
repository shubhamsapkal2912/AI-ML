#Calculate measures of dispersion from CSV data using Pandas.
import pandas as pd
# Load the dataset
data = pd.read_csv('iris.csv', header=None, names=['SepalLength', 'SepalWidth',
'PetalLength', 'PetalWidth', 'Species'])
# Variance, Standard Deviation, and Range for SepalWidth
variance = data['SepalWidth'].var()
std_dev = data['SepalWidth'].std()
data_range = data['SepalWidth'].max() - data['SepalWidth'].min()
print(f"Variance: {variance}, Standard Deviation: {std_dev}, Range: {data_range}")
