import numpy as np
#linear Algebra

# Matrix multipliation
print('Matrix multiplication')
print('we will multiply a 2x3 matrix with a 3x2 matrix which should give us a 2x2  matrix to be precise lets check it out with an example')
print('\n')
a =  np.ones((2,3), dtype='int16')
b = np.full((3,2),2,dtype='int16')
d = np.matmul(a,b)
print(d)
print('\n\n')


#finding determinant of a matrix
# we will  use a simple identity matrix in this cuz identity matrix has determinant 1
print('Finding Determinant')
print('\n')
c = np.identity(4)
print(np.linalg.det(c))
print('\n\n')


#finding minimuum
print('Finding Minimum')
print('\n')
print(np.min(c))
print('\n\n')

#finding maximum
print('Finding Maximum')
print('\n')
print(np.max(c))
print('\n')

#you can do more just go on the site https://docs.scipy.org/doc/numpy/reference/routinesLinalg.html
print('')

#sum
np.sum(c)

#reorganizing arrays
print('\n')
before = np.array([[1,2,3,4],[5,6,7,8]], dtype='int16')
after = before.reshape((8,1))
print(after)

print('\n\n')

#Vertically Stacking Vectors
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
v3 = np.vstack((v1,v2,v1,v2))
print('Stacking two matrix')
print(v3)

#horizontally stacking
h1 = np.ones((2,4), dtype='int16')
h2 = np.zeros((2,2), dtype='int16')
h3 = np.hstack((h1,h2))
print('\n')
print('Horizontally Sttacking ')
print(h3)


