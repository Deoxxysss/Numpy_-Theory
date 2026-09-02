import numpy as np

#matrix determinant
a = np.array([[1,2],[4,5]])
print(np.linalg.det(a))
print('\n')

#dot product of two vectors
a = np.array([1,2,3])
b = np.array([3,4,5])
print(np.dot(a,b))
print('\n')

#Transpose of a matrix converts mxn to nxm
a = np.array([[1,2,3],[4,5,6]])
print(a.T)
print('\n')

#calculate the mod of a vector
a = np.array([1,2,3])
print(np.linalg.norm(a))
print('\n')

#multiplication of two matrices
a = np.array([[1,2],[4,5]])
b = np.array([[1,3],[5,7]])
print(a@b)