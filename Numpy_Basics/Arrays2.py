#initializing different types of arrays.

import numpy as np

# All Zeros Matrix
# np.zeros() function is used to create an array filled with zeros.
print('All Zeros Matrix')
print('')
a = np.zeros((3,4,2), dtype='int16')
print(a)
print('')


# All Ones Matrix
# np.ones() function is used to create an array filled with ones.
print('All Ones Matrix')
print('')
b = np.ones((3,4,2), dtype='int16')
print(b)
print('')

# Any Other Number Matrix
# np.full() function is used to create an array filled with any other number.
print('Any Other Number Matrix')
print('')
c = np.full((3,4,2), 7, dtype='int16')
print(c)
print('')

# Any Number Matrix(full_like)
print('Any Number Matrix(full_like)')
print('')
d = np.full_like(c, 9, dtype='int16') # this will create an output similar to np.full(c.shape, 9, dtype='int16')
print(d)
print('')

# Random Decimal Numbers Matrix
# np.random.rand() function is used to create an array filled with random decimal numbers.
print('Random Decimal Numbers Matrix')
print('')
e = np.random.rand(3,4,2)
print(e)
print('')
f = np.random.rand(3,4,2) * 100 # this will create an array filled with random decimal numbers between 0 and 100.
print(f)
g = np.random.random_sample(a.shape) # this will create an array filled with random decimal numbers between 0 and 1.
print(g)

# Random Integer Numbers Matrix
# np.random.randint() function is used to create an array filled with random integer numbers.
print('Random Integer Numbers Matrix')
print('')
h = np.random.randint(1, 100, size=(3,4,2), dtype='int16') # this will create an array filled with random integer numbers between 1 and 100.
print(h)
print('')

# Identity Matrix
print('Identity Matrix')
print('')
z = np.identity(3) # Returns an identity square matrix of 3x3.
print(z)



# Repeat an array
print('Repeating an Array')
arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3, axis=0)
print(r1)
print('')

#copying an Array
print('Copying an array')
print('')
a = np.array([1,2,3], dtype='int16')
b = a.copy() #it will copy the whole a to b and if we cange b it will not change a
print('')

