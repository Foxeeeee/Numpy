import numpy as np

a = np.array([1,2,3,4])

print(a.sum())

b = np.array([[1,1],
              [2,2]])

print(b.sum(axis=0))
print(b.sum(axis=1))

data = np.array([1,2])
ones = np.ones(2)
print(data)
print(ones)
print(data + ones)
print(data * data)
print(data / data)
print(data * 3)
