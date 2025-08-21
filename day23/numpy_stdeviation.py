import numpy as np
a= np.array([[1,3,5],[2,4,6],[7,8,9]])
print("Original array: /n", a, "\n")

print("SD: \n", np.std(a), "\n")
print("SD by rows: \n", np.std(a,axis=1), "\n")
print("SD by columns: \n", np.std(a,axis=0), "\n")

