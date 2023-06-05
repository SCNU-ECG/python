import numpy as np
a = [0.5, 0.42, 0.31, 0.2, 0.11, 0, -0.3, -0.1, 0.03]
x = np.diff(a)

y = np.diff(x)
print(x)
print(y)