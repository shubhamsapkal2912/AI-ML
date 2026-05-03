#30 Write a Python program to implement ANOVA Test.
import pandas as pd
from scipy.stats import f_oneway
df = pd.read_csv("Mall_Customers.csv")
# Select columns and drop missing values
data = df[['Age', 'Annual Income (k$)']].dropna()
g1 = data['Age']
g2 = data['Annual Income (k$)']
f, p = f_oneway(g1, g2)
print("F-value:", f)
print("P-value:", p)