import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

x = np.arange(0, 20, 0.1)

for i in range(2, 12):
    plt.plot(x, stats.chi2.pdf(x, i+0.5), label='{}'.format(i))

plt.legend(loc='upper right')
plt.show()