import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

x = np.arange(0, 20, 0.1)

for i in range(1, 11):
    plt.plot(x, stats.chi2.pdf(x, i), label='{}'.format(i))

plt.legend(loc='upper right')
plt.show()