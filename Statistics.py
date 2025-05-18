from scipy import stats

# Generate random numbers from normal distribution
data = stats.norm.rvs(size=1000, loc=0, scale=1)

# Calculate descriptive statistics
mean, std = stats.norm.fit(data)
print(f"Mean: {mean:.2f}, Std: {std:.2f}")