import math
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science', 'ieee'])
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams["font.size"] = 16


file_path = '../data/bodysize.dat'

data = pd.read_csv(file_path, sep='\\s+', header=None, names=['Weight', 'Height', 'Chest'])
X = data[['Height', 'Chest']]
y = data['Weight']
X = sm.add_constant(X)

with open("../data/data.txt", "w") as f:
    for i in range(1, 25):
        poly = PolynomialFeatures(degree=i)
        X_poly = poly.fit_transform(X) # モデルをフィット
        poly_model = LinearRegression()
        poly_model.fit(X_poly, y)

        # 回帰係数とインターセプトを取得
        coefficients = poly_model.coef_
        intercept = poly_model.intercept_

        # モデルのR^2スコア
        r_squared = poly_model.score(X_poly, y)

        print(coefficients, intercept, r_squared, math.sqrt(r_squared))

        y_pred = poly_model.predict(X_poly)

        # print(y_pred)

        f.write(f"{i}, {r_squared}, {math.sqrt(r_squared)}\n")

        # プロット
        plt.figure(figsize=(10, 5))
        plt.scatter(y, y_pred, color='blue', label='Predicted vs. Actual')
        plt.xlabel('Actual Weight')
        plt.ylabel('Predicted Weight')
        plt.plot([y.min(), y.max()], [y.min(), y.max()], color='red', linestyle='--', linewidth=2, label='Ideal Fit')
        plt.legend()
        plt.grid(True)
        plt.savefig(f"../figures/polynomial_regression-n-{i}.png")
        plt.close()
