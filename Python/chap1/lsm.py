import numpy as np
import matplotlib.pyplot as plt

# 統計的機械学習の数理 最小二乗法
# https://scrapbox.io/natsutan0-82268433/%E6%9C%80%E5%B0%8F%E4%BA%8C%E4%B9%97%E6%B3%95

np.random.sample(1234)

def data_gen(N=100):
    N = 100
    a = np.random.normal(loc=2, scale=2, size=N)
    b = np.random.randn(1)
    x = np.random.randn(N)
    y = a * x + b + np.random.randn(N)
    return x, y


def min_sq(x, y):
    x_bar, y_bar = np.mean(x), np.mean(y)
    beta_1 = np.dot(x - x_bar, y - y_bar) / np.linalg.norm(x - x_bar) ** 2
    beta_0 = y_bar - beta_1 * x_bar
    return beta_1, beta_0


def main():
    x, y = data_gen()
    a1, b1 = min_sq(x, y)
    xx = x - np.mean(x)
    yy = y - np.mean(y)
    a2, b2 = min_sq(xx, yy)

    print(a1, b1)
    print(a2, b2)

    x_seq = np.arange(-5, 5, 0.1)
    y_pre = x_seq * a1 + b1
    yy_pre = x_seq * a2 + b2

    plt.scatter(x, y, c='black')
    plt.axhline(y=0, c='black', linewidth=0.5)
    plt.axvline(x=0, c='black', linewidth=0.5)
    plt.plot(x_seq, y_pre, c="blue", label="before centralization")
    plt.plot(x_seq, yy_pre, c='orange', label="after centralization")
    plt.legend(loc="upper left")
    plt.show()

if __name__ == '__main__':
    main()
