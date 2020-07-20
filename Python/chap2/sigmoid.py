import numpy as np
import matplotlib.pyplot as plt

beta_0 = 0

def sigmoid(x, beta):
    return np.exp(beta_0 + beta * x) / (1 + np.exp(beta_0 + beta * x))


beta_seq = np.array([0, 0.2, 0.5, 1, 2, 10])
x_seq = np.arange(-10, 10,  0.1)

plt.xlabel("x")
plt.ylabel("P(Y=1|X)")

for i in range (beta_seq.shape[0]):
    beta =  beta_seq[i]
    p = sigmoid(x_seq, beta)
    plt.plot(x_seq, p, label='{}'.format(beta))

plt.legend(loc="upper left")
plt.show()

