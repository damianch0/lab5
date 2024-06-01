from turtle import end_fill

import numpy as np

a = np.array([20, 30, 40, 50])
b = np.arange(4)
print(a)
print(b)

c = a - b
print(c)

print(b ** 2)

print(a)
a += b
print(a)
a -= b
print(a)
d = a * b

b = np.arange(3)
print(b)
print(np.exp(b))
print(np.sqrt(b))
c = np.array([2., -1., 4.])
print(np.add(b, c))

a = np.arange(12).reshape((3, 4))
print(a)
print(a.sum())
print(a.sum(axis=0))
print(a.min(axis=1))
print((a.cumsum(axis=1)))
print()
a = np.arange(3)
b = np.arange(3)
print(a)
print(b)
print(a.dot(b))
print(np.dot(a, b))
c = np.array([[1, 5], [2, 6], [7, 4]])
d = np.array([[2, 5, 4], [4, 3, 1]])
print(c)
print(d)
print(np.dot(c, d))
print(np.dot(d, c))

print()
a = np.arange(6).reshape((3, 2))
print(a)
print(a.shape)
print(type(a.shape))
for b in a:
    print(b)
print()
for i in range(0, a.shape[0]):
    for j in range(0, a.shape[1]):
        print(a[i][j], end=' ')
    print(" ")
print()
for b in a.flat:
    print(b)
print()
a = np.arange(6)
print(a)
print(a.shape)
print("")
b = a.reshape((2, 3))
print(b)
print(b.shape)
print("")
c = b.reshape((3, 2))
print(c)
print(c.shape)
print("")
d = c.ravel()
print(d)
print(d.shape)
print("")
e = b.T
print(e)
