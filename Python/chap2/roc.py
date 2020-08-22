import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

N_0 = 10000
N_1 = 1000

mu_1 = 1
mu_0 = -1
var_1 = 1
var_0 = 1

x = np.random.normal(mu_0, var_0, N_0)
y = np.random.normal(mu_1, var_1, N_1)

theta_seq = np.exp(np.arange(-10,100,0.1))

U = []
V = []

for i in range(len(theta_seq)-1):
    u = np.sum((stats.norm.pdf(x, mu_1, var_1)/stats.norm.pdf(x, mu_0, var_0)) > theta_seq[i]) / N_0
    v = np.sum((stats.norm.pdf(y, mu_1, var_1)/stats.norm.pdf(y, mu_0, var_0)) > theta_seq[i]) / N_1

    U.append(u)
    V.append(v)

AUC = 0.0
for i in range(len(theta_seq)-2):
    AUC = AUC + np.abs(U[i+1]-U[i])*V[i]

plt.plot(U,V)
plt.text(0.3, 0.5, "AUC={}".format(AUC), fontsize=15)
plt.show()

