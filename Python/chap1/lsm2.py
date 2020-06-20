# 重回帰バージョン
import numpy as np

n = 100
p = 2
beta = np.array([1, 2, 3])
x = np.random.randn(n, 2)

y = beta[0] + beta[1] * x[:, 0] + beta[2] * x[:, 1] + np.random.randn(n)

X = np.insert(x, 0, 1, axis=1) # 左にすべて１の列を置く
beta_hat = np.linalg.inv(X.T @ X) @ X.T @ y

print(beta_hat)