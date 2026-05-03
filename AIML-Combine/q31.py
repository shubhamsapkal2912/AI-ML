import numpy as np
from scipy import stats

# Sample data
data = np.array([12, 14, 15, 16, 14, 13, 15, 14, 16, 15])

# Population mean (hypothesis)
pop_mean = 14

# Perform one-sample t-test
t_stat, p_value = stats.ttest_1samp(data, pop_mean)

print("T-statistic:", t_stat)
print("P-value:", p_value)

# Decision
if p_value < 0.05:
    print("Reject Null Hypothesis")
else:
    print("Fail to Reject Null Hypothesis")