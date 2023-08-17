import numpy as np

data = np.array([1,2,3])
print(data[0])
print(data[1])
print(data[1:2])
print(data[2:])
print(data[-2:], '\n')

a = np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]])

print(a)
print(a[a >= 5], '\n')

five_up = (a >= 5)
print(a[five_up], '\n')

divisible_by_2 = a[a%2==0]
print(divisible_by_2, '\n')

c = a[(a > 2) & (a < 11)] 
print(c)
