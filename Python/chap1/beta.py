import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm

N = 100
x = np.random.randn(N).reshape(-1, 1)
y = np.random.randn(N).reshape(-1, 1)

X = np.insert(x, 0, 1, axis=1)
model = sm.OLS(y, X)
res = model.fit()

print(res.summary())