import pandas as pd
# Load the dataset
data = pd.read_csv(
    'iris.csv',
    header=None,
    names=['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species'],
    skiprows=1
)
# Correlation between SepalLength and PetalLength
correlation = data['SepalLength'].corr(data['PetalLength'])
print(f"Correlation Coefficient between SepalLength and PetalLength: {correlation}")