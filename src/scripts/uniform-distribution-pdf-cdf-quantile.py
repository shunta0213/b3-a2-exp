import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science', 'ieee'])
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams["font.size"] = 16

# データポイントの生成
x = np.linspace(-0.1, 1.1, 1000)

# 一様分布のPDF
pdf = np.where((x >= 0) & (x <= 1), 1, 0)

# 一様分布のCDF
cdf = np.where(x < 0, 0, np.where(x > 1, 1, x))

# 50パーセンタイルの計算
median = 0.3

# PDFのグラフ作成
plt.figure(figsize=(8, 6))
plt.plot(x, pdf, 'b-', label='PDF (Probability Density Function)')
plt.fill_between(x, pdf, where=(x >= 0) & (x <= 1), alpha=0.2)
plt.title('Probability Density Function of a Uniform Distribution on [0, 1]')
plt.xlabel('$x$')
plt.ylabel('Probability Density')
plt.ylim(0, 1.5)
plt.axvline(median, color='r', linestyle='--', label=f'Median at x = {median}')
plt.legend()

# PDFグラフを画像として保存
plt.savefig('../figures/uniform-distribution-pdf-cdf-quantile/uniform_pdf.png')
plt.close()

# CDFのグラフ作成
plt.figure(figsize=(8, 6))
plt.plot(x, cdf, 'g-', label='CDF (Cumulative Distribution Function)')
plt.title('Cumlative Distribution Function of a Uniform Distribution on [0, 1]')
plt.xlabel('$x$')
plt.ylabel('Cumulative Probability')
plt.axvline(median, color='r', linestyle='--', label='30th Percentile (Median)')
plt.axhline(median, color='r', linestyle='--')
plt.legend()

# CDFグラフを画像として保存
plt.savefig('../figures/uniform-distribution-pdf-cdf-quantile/uniform_cdf.png')
plt.close()


# 画像のパスを表示
