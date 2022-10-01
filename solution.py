import numpy as np

vector = np.vectorize(np.int_)
y = np.array([2, 4, 6, 8])
x = vector(y)

print(x)
# [2, 4, 6, 8]
