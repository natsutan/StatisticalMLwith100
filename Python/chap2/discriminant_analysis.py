import numpy as np
import matplotlib.pyplot as plt

#真のパラメータ
mu_1 = np.array([2, 2])
sigma_1 = 2
sigma_2 = 2
rho_1 = 0.5

mu_2 = np.array([-3, -3])
sigma_3 = 1
sigma_4 = 1
rho_2 = -0.8

# 真のパラメータに基づいてデータを発生
n = 100
u = np.random.randn(n)
v = np.random.randn(n)

x_1 = sigma_1 * u + mu_1[0]
#y_1 = (rho_1 * u * np.sqrt(1-rho_1**2)*v) * sigma_2 + mu_1[1]
y_1 = sigma_2 * v + mu_1[1]

u = np.random.randn(n)
v = np.random.randn(n)

x_2 = sigma_3 * u + mu_2[0]
#y_2 = (rho_2 * u * np.sqrt(1-rho_2**2)*v) * sigma_4 + mu_2[1]
y_2 = sigma_4 * v + mu_2[1]


mu_1 = np.average((x_1, y_1), 1)
mu_2 = np.average((x_2, y_2), 1)

xx = np.concatenate((x_1 - mu_1[0], x_2 - mu_2[0]), 0).reshape(-1, 1)
yy = np.concatenate((y_1 - mu_1[1], y_2 - mu_2[1]), 0).reshape(-1, 1)

df = np.concatenate((xx,yy), 1)
mat = np.cov(df, rowvar=0)

inv_1 = np.linalg.inv(mat)
de_1 = np.linalg.det(mat)

inv_2 = inv_1
de_2 = de_1

# 共分散行列が等しくないとき
#df = np.array([x_1, y_1])
#mat = np.cov(df, rowvar=1)
#inv_1 = np.linalg.inv(mat)
#de_1 = np.linalg.det(mat)

#df = np.array([x_2, y_2])
#mat = np.cov(df, rowvar=1)
#inv_2 = np.linalg.inv(mat)
#de_2 = np.linalg.det(mat)


def f(x, mu, inv, de):
    return -0.5 * (x - mu).T@inv@(x - mu) - 0.5 * np.log(de)


def f_1(u, v):
    return f(np.array([u, v]), mu_1, inv_1, de_1)


def f_2(u, v):
    return f(np.array([u, v]), mu_2, inv_2, de_2)

pi_1 = 0.5
pi_2 = 0.5
u = v = np.linspace(-6, 6, 50)
m = len(u)

w = np.zeros([m,m])
for i in range(m):
    for j in range(m):
        w[i, j] = np.log(pi_1) + f_1(u[i], v[j]) - np.log(pi_2) - f_2(u[i], v[j])


plt.contour(u, v, w, levels=0, colors=['black'])
plt.scatter(x_1, y_1, c="red")
plt.scatter(x_2, y_2, c="blue")

plt.show()
