import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm

N = 100


def min_sq(x, y):
    x_bar, y_bar = np.mean(x), np.mean(y)
    beta_1 = np.dot(x - x_bar, y - y_bar) / np.linalg.norm(x - x_bar) ** 2
    beta_0 = y_bar - beta_1 * x_bar
    return beta_1, beta_0


x = np.random.randn(N)
y = np.random.randn(N)

beta_1, beta_0 = min_sq(x, y)
RSS = np.linalg.norm(y-beta_0-beta_1*x)**2
RSE = np.sqrt(RSS/(N-2))

B_0 = (x.T@x/N)/np.linalg.norm(x-np.mean(x))**2
B_1 = 1/np.linalg.norm(x-np.mean(x))**2

se_0 = RSE * np.sqrt(B_0)
se_1 = RSE * np.sqrt(B_1)

t_0 = beta_0 / se_0
t_1 = beta_1 / se_1

t_0 = beta_0 / se_0
t_1 = beta_0 / se_1

p_0 = 2 * (1 - stats.t.cdf(np.abs(t_0), N-2))
p_1 = 2 * (1 - stats.t.cdf(np.abs(t_1), N-2))

print(beta_0, se_0, t_0, p_0)
print(beta_1, se_1, t_1, p_1)
print()

from sklearn import linear_model

reg = linear_model.LinearRegression()
x = x.reshape(-1, 1)
y = y.reshape(-1, 1)
reg.fit(x,y)
print(reg.coef_, reg.intercept_)

import statsmodels.api

X = np.insert(x,0,1,axis=1)
model = sm.OLS(y, X)
res = model.fit()

print(res.summary())
