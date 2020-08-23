import itertools

import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston

res = LinearRegression()


def RSS_min(X, y, T):
    s_min = np.inf
    m = len(T)
    for j in range(m):
        q=T[j]
        res.fit(X[:, q], y)
        y_hat = res.predict(X[:, q])
        S = np.linalg.norm(y_hat - y) ** 2
        if S < s_min:
            s_min = S
            set_q = q

    return (s_min, set_q)

boston = load_boston()
X = boston.data[:, [0, 2, 4, 5, 6, 7, 9, 10, 11, 12]]
y = boston.target

n, p = X.shape
AIC_min = np.inf
for k in range(1, p+1, 1):
    T = list(itertools.combinations(range(p), k))
    S_min, set_q = RSS_min(X, y, T)
    AIC = n * np.log(S_min/n) + 2 ** k
    if AIC < AIC_min:
        AIC_min = AIC
        set_min = set_q

print(AIC_min, set_min)


def IC(X, y, k):
    n, p = X.shape
    T = list(itertools.combinations(range(p), k))
    S, set_q = RSS_min(X, y, T)
    AIC = n * np.log(S/n) + 2 * k
    BIC = n * np.log(S/n) + k * np.log(n)

    return {'AIC':AIC, 'BIC':BIC}

AIC_seq = []
BIC_seq = []

for k in range(1, p+1, 1):
    AIC_seq.append(IC(X, y, k)['AIC'])
    BIC_seq.append(IC(X, y, k)['BIC'])

x_seq = np.arange(1, p+1, 1)
plt.plot(x_seq, AIC_seq, c='red', label="AIC")
plt.plot(x_seq, BIC_seq, c='blue', label="BIC")

plt.legend()

plt.show()

