import numpy as np

array_example = np.array([[[1,2,3,4],
                           [5,6,7,8],
                  
                           [1,2,3,4],
                           [5,6,7,8],
                           
                           [1,2,3,4],
                           [5,6,7,8]]])

a = np.arange(6)

print(array_example)
print(array_example.ndim)
print(array_example.size)
print(array_example.shape)
print(a.reshape(3,2))