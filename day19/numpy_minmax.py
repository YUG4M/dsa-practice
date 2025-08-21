import numpy as np
a= np.array([[1,3,5],[2,4,6],[7,8,9]])
print("Original array: /n", a, "\n")

print("Minimum of all elements: \n", np.min(a), "\n")
print("Minimum of all elements by rows: \n", np.min(a,axis=1), "\n")
print("Minimum of all elements by columns: \n", np.min(a,axis=0), "\n")

print("Maximum of all elements: \n", np.max(a), "\n")
print("Maximum of all elements by rows: \n", np.max(a,axis=1), "\n")
print("Maximum of all elements by columns: \n", np.max(a,axis=0), "\n")
