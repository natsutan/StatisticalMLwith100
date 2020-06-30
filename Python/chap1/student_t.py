import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

x = np.arange(-10, 10, 0.1)
plt.plot(x, stats.norm.pdf(x, 0, 1), label="norm", c="black", linewidth=1)

for i in range(1, 10):
    plt.plot(x, stats.t.pdf(x,i), label='{}'.format(i))

plt.legend(loc='upper right')
plt.show()