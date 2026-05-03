#31 Perform t-Test
import pandas as pd
from scipy.stats import ttest_ind
# Load dataset
df = pd.read_csv("Mall_Customers.csv")
# Select numeric columns and remove missing values
data = df[['Age', 'Annual Income (k$)']].dropna()
g1 = data['Age']
g2 = data['Annual Income (k$)']
# t-Test
t_stat, p_val = ttest_ind(g1, g2)
print("t-value:", t_stat)
print("p-value:", p_val)