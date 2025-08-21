import numpy as np
a= np.array([3,2,4,1])
print("Original array: \n", a)
sort= np.sort(a)
print("New array: \n", sort)
a.sort()
print("by sort function: \n", a)