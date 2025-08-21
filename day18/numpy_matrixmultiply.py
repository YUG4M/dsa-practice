import numpy as np
x= np.array([[1,2],[3,4]])
y= np.ones((2,2))
z= np.array([6,7])

print("Shape of the array z: \n", np.shape(z), '\n')

print("Shape of the array x: \n", np.shape(x), '\n')

print("z X x: \n")
print(np.dot(z,x))

print("x X z: \n")
print(np.dot(x,z))