#write a py program to find the sum of all the diagonal elements of a 4x4 multi dimensional array, without using any inbuilt function of numpy
import numpy as np
myarray= [[1,2,3,4],[5,6,7,8,],[9,19,11,12],[13,14,15,16]]
rows=len(myarray)
a=0
for i in range(rows):
    a+= myarray[i][i]
print(a)