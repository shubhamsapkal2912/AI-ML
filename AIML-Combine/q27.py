import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset
data = pd.read_csv('iris.csv', header=None, names=['SepalLength', 'SepalWidth',
'PetalLength', 'PetalWidth', 'Species'])
# Frequency Table
frequency_table = data['Species'].value_counts()
print(frequency_table)
# Bar Plot
frequency_table.plot(kind='bar', color='skyblue')
plt.title("Frequency Distribution of Species")
plt.xlabel("Species")
plt.ylabel("Count")
plt.show()
