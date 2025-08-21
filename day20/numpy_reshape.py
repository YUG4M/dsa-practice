import numpy as np
a = np.array([[1,2,3],[4,5,6],[9,8,7]])
print("Original Array: \n", a, "\n")

b= a.reshape(1,9)

print("Reshaped Array: \n", b, "\n")
print("Reshaped Array Shape: \n", b.shape)