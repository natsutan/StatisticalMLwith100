import numpy as np
import matplotlib.pyplot as plt

n = 100
p = 5
X = np.insert(np.random.randn(n, p), 0, 1, axis=1)
beta = np.random.randn(p+1).reshape(-1, 1)
y = X@beta+0.2*np.random.randn(n).reshape(-1, 1)
y = y[:, 0]


def cv_liner(X, y, K):
    n = len(y)
    m = int(n/K)
    S = 0
    for j in range(K):
        test = list(range(j*m, (j+1)*m))
        train = list(set(range(n))-set(test))
        beta = np.linalg.inv(X[train,].T@X[train,])@X[train,].T@y[train]
        e = y[test] - X[test,]@beta
        S = S + np.linalg.norm(e) ** 2

    return S/n

def cv_fast(X, y, K):
    n = len(y)
    m = n / K
    H = X@np.linalg.inv(X.T@X)@X.T
    I = np.diag(np.repeat(1,n))
    e = (I-H)@y
    I = np.diag(np.repeat(1,m))
    S = 0
    for j in range(K):
        test = np.arange(j*m, (j+1)*m, 1, dtype=int)
        S=S+(np.linalg.inv(I-H[test,test])@e[test]).T@np.linalg.inv(I-H[test,test])@e[test]

    return S/n

#ret = cv_liner(X, y, 10)
#print(ret)
#ret = cv_fast(X, y, 10)
#print(ret)

plt.ylim(0,3, 1.5)

for j in range(2,11,1):
    X = np.random.randn(n,p)
    X = np.insert(X, 0, 1, axis=1)
    beta = np.random.randn(p+1)
    y = X@beta+np.random.randn(n)
    U = []
    V = []
    for k in range(2,n+1,1):
        if n%k == 0:
            U.append(k)
            ret = cv_liner(X, y, k)
            V.append(ret)

    plt.plot(U, V)

plt.show()
