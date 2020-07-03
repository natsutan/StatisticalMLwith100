import numpy as np
from sklearn.datasets import load_boston

def R2(x,y):
    n = x.shape[0]
    xx = np.insert(x,0,1,axis=1)
    beta = np.linalg.inv(xx.T@xx)@xx.T@y
    y_hat = xx@beta
    y_bar = np.mean(y)
    RSS = np.linalg.norm(y-y_hat)**2
    TSS = np.linalg.norm(y-y_bar)**2

    return 1 - RSS/TSS


def VIF(x):
    p = x.shape[1]
    values = []
    for j in range(p):
        S = list(set(range(p))-{j})
        values.append((1/(1-R2(x[:,S],x[:,j]))))

    return values

boston = load_boston()
x = boston.data
print(VIF(x))
