import numpy as np
a= np.array([[1,3,5],[2,4,6],[7,8,9]])
print("Original array: /n", a, "\n")

print("Mean: \n", a.mean(), "\n")
print("Mean of rows: \n", a.mean(axis=1), "\n")
print("Mean of columns: \n", a.mean(axis=0), "\n")
