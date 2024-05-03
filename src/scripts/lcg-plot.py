import matplotlib.pyplot as plt
import pandas as pd
import scienceplots

plt.style.use(['science', 'ieee'])
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.fontset'] = 'stix'

num_2_16 = pd.read_csv("../data/zx/lcg_2_16.txt")
plt.hist(num_2_16, bins=100, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.savefig('../figures/lcg-plot/zx/lcg-2-16.png')
plt.close()

num_2_4 = pd.read_csv("../data/zx/lcg_2_4.txt")
plt.hist(num_2_4, bins=100, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.savefig('../figures/lcg-plot/zx/lcg-2-4.png')
plt.close()

num_2_8 = pd.read_csv("../data/zx/lcg_2_8.txt")
plt.hist(num_2_8, bins=100, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.savefig('../figures/lcg-plot/zx/lcg-2-8.png')
plt.close()

num_2_12 = pd.read_csv("../data/zx/lcg_2_12.txt")
plt.hist(num_2_12, bins=100, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.savefig('../figures/lcg-plot/zx/lcg-2-12.png')
plt.close()



num_rand_2_16 = pd.read_csv("../data/rand/lcg_2_16.txt")
plt.hist(num_rand_2_16, bins=100, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.savefig('../figures/lcg-plot/rand/lcg-2-16.png')
plt.close()

num_rand_2_4 = pd.read_csv("../data/rand/lcg_2_4.txt")
plt.hist(num_rand_2_4, bins=100, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.savefig('../figures/lcg-plot/rand/lcg-2-4.png')
plt.close()

num_rand_2_8 = pd.read_csv("../data/rand/lcg_2_8.txt")
plt.hist(num_rand_2_8, bins=100, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.savefig('../figures/lcg-plot/rand/lcg-2-8.png')
plt.close()

num_rand_2_12 = pd.read_csv("../data/rand/lcg_2_12.txt")
plt.hist(num_rand_2_12, bins=100, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.savefig('../figures/lcg-plot/rand/lcg-2-12.png')
plt.close()


num_rand_2_2_16 = pd.read_csv("../data/rand2/lcg_2_16.txt")
plt.hist(num_rand_2_2_16, bins=100, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.savefig('../figures/lcg-plot/rand2/lcg-2-16.png')
plt.close()

num_rand_2_2_4 = pd.read_csv("../data/rand2/lcg_2_4.txt")
plt.hist(num_rand_2_2_4, bins=100, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.savefig('../figures/lcg-plot/rand2/lcg-2-4.png')
plt.close()

num_rand_2_2_8 = pd.read_csv("../data/rand2/lcg_2_8.txt")
plt.hist(num_rand_2_2_8, bins=100, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.savefig('../figures/lcg-plot/rand2/lcg-2-8.png')
plt.close()


num_rand_2_2_12 = pd.read_csv("../data/rand2/lcg_2_12.txt")
plt.hist(num_rand_2_2_12, bins=100, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.savefig('../figures/lcg-plot/rand2/lcg-2-12.png')
plt.close()
