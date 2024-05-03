import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science', 'ieee'])
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams["font.size"] = 16

data = pd.read_csv('../../data/nba-2022-2023.csv', encoding='ISO-8859-1', delimiter=';')

# Pos列を数値に変換
label_encoder = LabelEncoder()
data['Pos'] = label_encoder.fit_transform(data['Pos'])
data['Player'] = label_encoder.fit_transform(data['Player'])
data['Tm'] = label_encoder.fit_transform(data['Tm'])

features = ['Age', 'Pos', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', 'FT', 'FTA', 'FT%']
X = data[features]
y = data['PTS']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

r2_score = model.score(X_test, y_test)
print(f'R^2 Score: {r2_score}')


# テストセットでの予測
y_pred = model.predict(X_test)

plt.figure(figsize=(8, 6))
# 実際の値と予測値のプロット
plt.scatter(y_test, y_pred, alpha=0.7)
plt.xlabel("Actual PTS")
plt.ylabel("Predicted PTS")

plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red')
plt.grid(True)
plt.savefig(f"../../figures/nba-regression/actual-vs-predicted-PTS.png")
plt.close()


# 説明変数と目的変数を定義
features = ['MP', 'Age', 'STL', 'BLK']
X = data[features]
y = data['PTS']
# トレーニングセットとテストセットに分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# モデルの作成と学習
model = LinearRegression()
model.fit(X_train, y_train)
r2_score = model.score(X_test, y_test)
r2_score
print(f'R^2 Score: {r2_score}')
y_pred = model.predict(X_test)
plt.figure(figsize=(8, 6))
# 実際の値と予測値のプロット
plt.scatter(y_test, y_pred, alpha=0.7)
plt.xlabel("Actual PTS")
plt.ylabel("Predicted PTS")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red')
plt.grid(True)
plt.savefig(f"../../figures/nba-regression/actual-vs-predicted-PTS-2.png")
plt.close()

# PTS以外の全てのデータを使用
X = data.drop(columns=['PTS'])
y = data['PTS']
# トレーニングセットとテストセットに分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# モデルの作成と学習
model = LinearRegression()
model.fit(X_train, y_train)
# モデルの性能を評価
r2_score = model.score(X_test, y_test)
r2_score
print(f'R^2 Score: {r2_score}')
y_pred = model.predict(X_test)
plt.figure(figsize=(8, 6))
# 実際の値と予測値のプロット
plt.scatter(y_test, y_pred, alpha=0.7)
plt.xlabel("Actual PTS")
plt.ylabel("Predicted PTS")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red')
plt.grid(True)
plt.savefig(f"../../figures/nba-regression/actual-vs-predicted-PTS-3.png")
plt.close()
