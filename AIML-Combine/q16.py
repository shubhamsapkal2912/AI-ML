# Import required libraries
import pandas as pd
from scipy import stats

# Load the dataset
data = pd.read_csv(
    'iris.csv',
    header=None,
    names=['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']
)

# Calculate mean, median, and mode for SepalLength
mean = data['SepalLength'].mean()
median = data['SepalLength'].median()
mode = stats.mode(data['SepalLength'])

# Display results
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode.mode[0]}")