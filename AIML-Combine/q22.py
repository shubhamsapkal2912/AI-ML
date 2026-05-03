import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset
data = pd.read_csv('iris.csv', header=None, names=['SepalLength', 'SepalWidth',
'PetalLength', 'PetalWidth', 'Species'])
# Histogram
plt.hist(data['PetalLength'], bins=10, color='blue', alpha=0.7)
plt.title("Histogram of PetalLength")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")
plt.show()
# Box Plot
plt.boxplot(data['PetalLength'])
plt.title("Box Plot of PetalLength")
plt.ylabel("Petal Length (cm)")
plt.show()