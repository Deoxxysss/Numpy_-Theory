##Miscellaneous##
#Load Data From Files#
import numpy as np

#1 If the Data is separated by commas and is a txt file
filedata = np.genfromtxt('test.txt', delimiter=',') #the values in the array will be of float type
filedata = filedata.astype('int32') #now it is in int form
print(filedata)
print('\n')

###Advanced Indexing and Boolean Masking###

h = np.random.randint(1, 100, size=(8,4), dtype='int16')
print(h > 50) #returns an array with True and False with the condition applied
print('\n')
print(h[h>50])  # Returns the value in the array which is greater than 50
# similarly we can use >= <= and much more..
print('\n')
print((h>50)&(h<80)) # do (~(h>50)&(h<80)) to get the opposite output
print('\n')
#you can also do np.all and np.any with axis = 0 to check which column in the array has any or all the values greater than x


# cool indexing 
# we can pass in list of position vector to get the value we want>
a = np.array([1,2,3,4,5,6,7,8,9], dtype='int16')
print(a[[1,4,6,7]]) #it will print all the values that are in the position 1,4,6,7
print('\n')
