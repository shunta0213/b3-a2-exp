import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import scienceplots

plt.style.use(['science', 'ieee'])
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams["font.size"] = 16

# データポイントの生成
x = np.linspace(-3, 3, 1000)

# 標準正規分布のPDF
pdf = norm.pdf(x)

# 標準正規分布のCDF
cdf = norm.cdf(x)

# 30パーセンタイルの計算
percentile_30 = norm.ppf(0.3)

# PDFのグラフ作成
plt.figure(figsize=(8, 6))
plt.plot(x, pdf, 'b-', label='PDF')
plt.fill_between(x, pdf, alpha=0.2)
plt.axvline(percentile_30, color='r', linestyle='--', label=f'30th Percentile at x = {percentile_30:.2f}')
plt.title('Probability Density Function of a Standard Normal Distribution')
plt.xlabel('$x$')
plt.ylabel('Probability Density')
plt.legend()
plt.savefig('../figures/pdf-cdf-quantile/pdf-quantile.png')  # PDFグラフを画像として保存
plt.close()  # グラフをクローズ

# CDFのグラフ作成
plt.figure(figsize=(8, 6))
plt.plot(x, cdf, 'g-', label='CDF')
plt.axhline(0.3, color='r', linestyle='--', label='30th Percentile')
plt.axvline(percentile_30, color='r', linestyle='--')
plt.title('Cumulative Distribution Function of a Standard Normal Distribution')
plt.xlabel('$x$')
plt.ylabel('Cumulative Probability')
plt.legend()
plt.savefig('../figures/pdf-cdf-quantile/cdf-quantile.png')  # CDFグラフを画像として保存
plt.close()  # グラフをクローズ
