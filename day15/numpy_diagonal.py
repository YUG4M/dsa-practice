import numpy as np

a = np.matrix([[1,2,3],[4,5,6],[9,8,7]])
print(a, "\n")

print(np.diag(a))
print(np.diag(a,1))
print(np.diag(a,2))
