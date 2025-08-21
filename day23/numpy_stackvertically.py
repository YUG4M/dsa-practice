import numpy as np

x= np.arange(10).reshape(2,-1)
y= np.arange(10,15).reshape(1,-1)

print("1st array is: \n", x, "\n")
print("2nd array is: \n", y, "\n")

print("Combined array is: \n", np.concatenate([x,y], axis=0))