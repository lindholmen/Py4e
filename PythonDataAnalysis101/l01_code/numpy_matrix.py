import numpy as np
import numpy.linalg as la
import time

X = np.array([range(0, 500), range(500, 1000)])
m, n = X.shape
print(m, n)

'''
D(i, j) = ||xi - xj||^2
'''
t = time.time()
D = np.zeros([n, n])
for i in range(n):
    for j in range(i + 1, n):
        D[i, j] = la.norm(X[:, i] - X[:, j]) ** 2
        D[j, i] = D[i, j]
print(time.time() - t)

'''
|xi - xi| = sqrt((xi - xj) * (xi - xj).T)
D(i, j) = (xi - xj) * (xi - xj).T
'''
t = time.time()
D = np.zeros([n, n])
for i in range(n):
    for j in range(i + 1, n):
        d = X[:, i] - X[:, j]
        D[i, j] = np.dot(d, d)
        D[j, i] = D[i, j]
print(time.time() - t)

'''
D(i, j) = (xi - xj) * (xi - xj).T
        = xi * xi.T - xi * xj.T - xj * xi.T + xj * xj.T
        = xi * xi.T - 2 * xi * xj.T + xj * xj.T
G(i,j) = xi.T * xj
'''
t = time.time()
G = np.dot(X.T, X)
D = np.zeros([n, n])
for i in range(n):
    for j in range(i + 1, n):
        D[i, j] = G[i, i] - G[i, j] * 2 + G[j,j]
        D[j, i] = D[i, j]
print(time.time() - t)

'''
H(i, j) = G(i, i)
K(i, j) = G(j, j) = H(i, j).T
D(i, j) = H(i, j) + K(i, j) - 2 * G(i, j)
'''
t = time.time()
G = np.dot(X.T, X)
H = np.tile(np.diag(G), (n, 1)) # n rows, 1 for each row
D = H + H.T - G * 2
print(time.time() - t)
