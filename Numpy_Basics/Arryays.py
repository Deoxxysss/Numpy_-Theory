import numpy as np
import sys

#how to define an array in numpy
#np.array() function is used to define an array in numpy
a = np.array([1, 2, 3])
print('')
b = np.array([[4.0, 5.0, 6.0], [2.0, 3.0, 4.0]])
print(a)
print('\n')
print(b)
print('')

#how to get the dimension of an array
# .ndim attribute is used to get the dimension of an array
print(a.ndim)
print(b.ndim)
print('')


#how to get the shape of an array
# .shape attribute is used to get the shape of an array
# we call a matrix with m rows and n columns as a m x n matrix
print(a.shape)
print(b.shape)
print('')


#how to get the type of an array
# .dtype attribute is used to get the type of an array
# initial default data type of an array is int32 or int64 depending on the system architecture
print(a.dtype)
print(b.dtype)
print('')


# To specify the data type of an array, we can use the dtype argument in the np.array() function
# we use dtype argument to specify the data type of an array
# Lowering the type means it will take less space
a = np.array([1, 2, 3], dtype='int16')
b = np.array([[4.0, 5.0, 6.0], [2.0, 3.0, 4.0]], dtype='float32')
print(a.dtype)
print(b.dtype)
print('')


# To Get the size of an array.
# We use the .itemsize attribute to get the size of an array in bytes. int16 takes 2 bytes and float32 takes 4 bytes
print(a.itemsize)
print(b.itemsize)
print('')

# To get the total number of elements in an array.
# We use the .size attribute to get the total number of elements in an array.
print(a.size)
print(b.size)
print('')

# To get the total number of bytes consumed by an array.
# We use the .nbytes attribute to get the total number of bytes consumed by an array
print(a.nbytes)
print(b.nbytes)
print('')

# To get a specific element from the array.
# We can use indexing to get a specific element from the array. Indexing starts from 0.
# We can also use negative indexing to get elements from the end of the array. -1 refers to the last element, -2 refers to the second last element and so on.
print(b[1, 2]) # gets the element from second row and third column of the array b
print(b[0, 1]) # gets the element from first row and second column of the array b
print(b[-1, -1]) # gets the element from the last row and last column of the array b
print('')

# To get a specific row or column from the array.
print(b[1, :]) # gets the second row of the array b
print(b[:, 2]) # gets the third column of the array b
print('')

# Some patterns
print(b[0, 0::2]) # gets the first row of the array b and every second element starting from the first element
print('')

# To replace a element in the array.
a[1] = 10 # replaces the second element of the array a with 10
b[0, 1] = 20 # replaces the element in the first row and second column of the array b with 20
print(a)
print(b)
print('')

# 3-D array
c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], dtype='int16')
print(c)
print(c.ndim)
print(c.shape)  
print('')

# To get a specific element from the array.
# We can use indexing to get a specific element from the array. Indexing starts from 0.
print(c[1,0,1])# gets the element from second block, first row and second column of the array c ie. 8.
print(c[:,1,:]) # gets the second row of both blocks of the array c
print('')

#replace
c[:,0,:] = [[13,14,15], [16,17,18]] # replaces the first row of both blocks of the array c with new values
print(c)
c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], dtype='int16')
print('')

#END OF THIS FILE