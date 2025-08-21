import numpy as np
a= np.array([[3,2,4],[7,2,8],[1,5,8]])
print("Original array: /n", a, "\n")
a= np.sort(a, axis=1)
print("Sort by rows: \n", a,"\n")
a= np.sort(a, axis=0)
print("Sort by columns: \n", a,"\n")