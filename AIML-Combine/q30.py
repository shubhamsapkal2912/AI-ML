from scipy.stats import f_oneway

# Sample data (3 groups)
group1 = [10, 12, 14, 16, 18]
group2 = [20, 22, 24, 26, 28]
group3 = [30, 32, 34, 36, 38]

# Perform ANOVA
f_stat, p_value = f_oneway(group1, group2, group3)

# Output results
print("F-Statistic:", f_stat)
print("P-Value:", p_value)

# Interpretation
if p_value < 0.05:
    print("Reject Null Hypothesis (Means are different)")
else:
    print("Fail to Reject Null Hypothesis (Means are similar)")