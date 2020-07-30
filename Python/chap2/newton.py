import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2-1

def df(x):
    return 2*x

x_seq = np.arange(-1, 5, 0.1)
f_x = f(x_seq)

plt.plot(x_seq, f_x)
plt.axhline(y=0, c="black", linewidth=0.5)
plt.xlabel("x")
plt.ylabel("y")
x = 4

for i in range(10):
    X = x
    Y = f(x)
    x = x - f(x) / df(x)
    y = f(x)
    plt.plot([X, x], [Y, 0], c="black", linewidth=0.8)
    plt.plot([X, X], [Y, 0], c="black", linewidth=0.8)
    plt.scatter(x, 0, c="red")

plt.show()

