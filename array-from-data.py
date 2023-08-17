import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])

arr1 = arr[3:8]
print(arr1)

a1 = np.array([[1,1],
               [2,2]])

a2 = np.array([[3,4],
               [4,4]])

print(np.vstack((a1,a2)))
print(np.hstack((a1,a2)))