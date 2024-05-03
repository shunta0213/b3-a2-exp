import matplotlib.pyplot as plt
import pandas as pd
import scienceplots

plt.style.use(['science', 'ieee'])

data = pd.read_csv("./linear-cogruential-generator/go/lcg_fuzz_results.txt", header=None, names=["seed", "a", "c", "m", "cycle"])

# Group data by 'a', 'c', 'm' and calculate statistical measures for 'cycle'
grouped_data = data.groupby(['a', 'c', 'm'])['cycle'].agg(['mean', 'max', 'min', 'median', 'count']).reset_index()

# Displaying the first few rows of the grouped data to understand the distribution
grouped_data.head()

# Plotting the impact of 'a', 'c', 'm' on the 'cycle' with applied styles
fig, axs = plt.subplots(3, 1, figsize=(10, 15))

# Plotting the mean cycles for different 'a' values
grouped_by_a = grouped_data.groupby('a')['mean'].mean().reset_index()
axs[0].plot(grouped_by_a['a'], grouped_by_a['mean'], marker='o', linestyle='-', color='r')
axs[0].set_title('Average Cycle by a')
axs[0].set_xlabel('a')
axs[0].set_ylabel('Average Cycle')
axs[0].grid(True)

# Plotting the mean cycles for different 'c' values
grouped_by_c = grouped_data.groupby('c')['mean'].mean().reset_index()
axs[1].plot(grouped_by_c['c'], grouped_by_c['mean'], marker='o', linestyle='-', color='g')
axs[1].set_title('Average Cycle by c')
axs[1].set_xlabel('c')
axs[1].set_ylabel('Average Cycle')
axs[1].grid(True)

# Plotting the mean cycles for different 'm' values
grouped_by_m = grouped_data.groupby('m')['mean'].mean().reset_index()
axs[2].plot(grouped_by_m['m'], grouped_by_m['mean'], marker='o', linestyle='-', color='b')
axs[2].set_title('Average Cycle by m')
axs[2].set_xlabel('m')
axs[2].set_ylabel('Average Cycle')
axs[2].grid(True)

plt.tight_layout()
plt.savefig("fig.png")
