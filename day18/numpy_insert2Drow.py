import numpy as np
a= np.array([[1,2],[3,4]])
print("The original array: \n", a)
a= np.insert(a,1,[11,12], axis=0)
print("The new array: \n", a)