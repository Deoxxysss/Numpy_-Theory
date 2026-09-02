##Question 2##
##ADVANCED INDEXING##
import numpy as np

a = np.arange(1, 31).reshape(6, 5)

print(a[2:4,0:2]) #PART1
print([a[0,1],a[1,2],a[2,3],a[3,4]])#part2
#or we can use
print(a[[0,1,2,3],[1,2,3,4]]) #first list contains the rows and the second list contains the columns
print(a[[0,0,4,4,5,5],[3,4,3,4,3,4]]) #part3
#or we can do
print(a[[0,4,5],3:])