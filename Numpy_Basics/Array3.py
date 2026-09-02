# Problem1
print('Keith Galli Numpy tutorials pproblem no 1 solution')
import numpy as np
i=0
j=0
a = np.zeros((5,5), dtype='int16')
for i in range(5):
    for j in range(5):
        if i == 0 or j == 0:
            a[i,j] = 1
        elif i ==4 or j == 4:
            a[i,j] = 1
        elif i==j and j==2:
            a[i,j] = 9
        a[i,j] = a[i,j]
print(a)
print('')

#Keith Galli Solution:
print('Keith Galli Solution')
print('')
output = np.ones((5,5), dtype='int16')

z = np.zeros((3,3), dtype='int16')
z[1,1] = 9

output[1:-1,1:-1] = z
print(output)
print('')

#Arthematic Operations
print('Arthematic Operations')
a = np.array([1,2,3,4,5], dtype='int32')


print('Sum')
print(a+2)
print('')


print('Substraction')
print(a-2)
print('')


print('Multiplication')
print(a*2)
print('')


print('Division')
print(a/2)
print('')


print('floor Division')
print(a//2)
print('')


print('Power')
print(a**2)
print('')


print('Take the sin')
print(np.sin(a))
print('')
#you can also use cos tan sec cosec etc.

