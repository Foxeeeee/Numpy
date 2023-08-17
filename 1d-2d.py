import numpy as np

a1 = np.array([1,2,3,4,5,6])
print(a1.shape)

a2 = a1[np.newaxis]
print(a2)
print(a2.shape, '\n')

row_vector = a1[np.newaxis, :]
print(row_vector)
print(row_vector.shape, '\n')

col_vector = a1[:, np.newaxis]
print(col_vector)
print(col_vector.shape, '\n')

b = np.expand_dims(a1, axis=1)
print(b.shape, '\n')

c = np.expand_dims(a1, axis=0)
print(c.shape)