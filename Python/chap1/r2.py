import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm

N = 10
m = 1

def R2(x, y):
    xx = np.insert(x, 0, 1, axis=1)
    beta = np.linalg.inv(xx.T@xx)@xx.T@y
    y_hat = xx@beta
    y_bar = np.mean(y)
    RSS = np.linalg.norm(y-y_hat)**2
    TSS = np.linalg.norm(y-y_bar)**2
    print(RSS, TSS)

    return 1 - RSS/TSS


x = np.random.randn(N, m)
y = np.random.randn(N)

print(R2(x,y))

x = x.reshape(-1)

print(np.corrcoef(x,y))