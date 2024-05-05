import matplotlib.pyplot as plt
import pandas as pd
import scienceplots

plt.style.use(['science', 'ieee'])
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.fontset'] = 'stix'


data = pd.read_csv("../data/tausworthe/fuzz.txt")

plt.hist(data, bins=100, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.savefig('../figures/tausworthe/tausworthe.png')
