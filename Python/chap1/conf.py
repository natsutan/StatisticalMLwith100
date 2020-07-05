import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

N = 100
p = 1
X = np.random.randn(N, p)
X = np.insert(X, 0, 1, axis=1)
beta = np.array([1, 1])
epsilon = np.random.randn(N)
y = X @ beta + epsilon

U = np.linalg.inv(X.T@X)
beta_hat = U@X.T@y
RSS = np.linalg.norm(y-X@beta_hat)**2
RSE = np.sqrt(RSS/(N-p-1))
alpha = 0.05


def f(x, a):
    x = np.array([1, x])
    r = stats.t.ppf(0.975, df=N-p-1) * RSE *np.sqrt(a+x@U@x.T)
    lower = x@beta_hat - r
    upper = x@beta_hat + r
    return [lower, upper]

x_seq = np.arange(-10, 10, 0.1)

#信頼区間
lower_seq1 = []
upper_seq1 = []

for i in range(len(x_seq)):
    lower_seq1.append(f(x_seq[i], 0)[0])
    upper_seq1.append(f(x_seq[i], 0)[1])

lower_seq2 = []
upper_seq2 = []
for i in range(len(x_seq)):
    lower_seq2.append(f(x_seq[i], 1)[0])
    upper_seq2.append(f(x_seq[i], 1)[1])

yy = beta_hat[0]+beta_hat[1]*x_seq

plt.xlim(np.min(x_seq), np.max(x_seq))
plt.ylim(np.min(lower_seq1), np.max(upper_seq1))
plt.plot(x_seq, yy, c='black')
plt.plot(x_seq, lower_seq1, c="blue")
plt.plot(x_seq, upper_seq1, c="red")
plt.plot(x_seq, lower_seq2, c="blue", linestyle="dashed")
plt.plot(x_seq, upper_seq2, c="red", linestyle="dashed")
plt.xlabel("x")
plt.xlabel("y")
plt.show()



