from math import *
import numpy
from scipy.sparse.csgraph import minimum_spanning_tree


def checkConnection(matrix, n, v, visited, path):
    if len(path) == n:
        return True
    for u in range(n):
        if matrix[v][u] != 0:
            if not visited[u]:
                path.append(u)
                visited[u] = True
                if checkConnection(matrix, n, u, visited, path):
                    return True
    return False


def cycle(matrix, last, visited, n, i, j):
    visited[i] = True
    for j in range(n):
        if matrix[i][j] > 0:
            if last != j:
                if visited[j]:
                    return False
                else:
                    cycle(matrix, i, visited, n, j, 0)
    return True


def spanningTree(matrix, mat, n):
    counter = 0
    min = 999
    imin = 999
    jmin = 999
    while counter < n - 1:
        min = 999
        for i in range(n):
            for j in range(n):
                if matrix[i][j] != 0 and matrix[i][j] < min:
                    min = matrix[i][j]
                    imin = i
                    jmin = j

        visited = [False] * n
        matrix[imin][jmin] = 0
        matrix[jmin][imin] = 0
        mat[imin][jmin] = 1
        mat[jmin][imin] = 1

        if not cycle(mat, -1, visited, n, imin, 0):
            mat[imin][jmin] = 0
            mat[jmin][imin] = 0
        else:
            counter += 1
    return mat


def findPrufer(matrix, n):
    prufer = []
    deg = [0] * n

    for i in range(n):
        for j in range(n):
            deg[i] += 1 if matrix[i][j] != 0 else 0

    while len(prufer) < n - 2:
        for i in range(n):
            if deg[i] == 1:
                break
        for j in range(n):
            if matrix[i][j] != 0:
                break
        prufer.append(j + 1)
        deg[i] = 0
        deg[j] -= 1
        matrix[i][j] = 0
        matrix[j][i] = 0

    print("Pruferov kod minimalnog razapinjuceg stabla: (", end="")
    print(*prufer, sep=", ", end="")
    print(")")


n = int(input("Unesite prirodan broj n: "))
a = int(input("Unesite prirodan broj a: "))
b = int(input("Unesite prirodan broj b: "))
c = int(input("Unesite prirodan broj c: "))

matrix = numpy.zeros((n, n))
mat = numpy.zeros((n, n))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i < j:
            weight = floor(abs(a * i - b * j) / c)
            if weight != 0:
                matrix[i - 1][j - 1] = weight
                matrix[j - 1][i - 1] = weight

# provjerava povezanost
visited = [False] * n
visited[0] = True
path = [0]
connected = checkConnection(matrix, n, 0, visited, path)

print("Graf G je povezan graf" if connected else "Graf G nije povezan graf")

if connected:
    mintreematrix = spanningTree(matrix, mat, n)
    findPrufer(mintreematrix, n)
else:
    print("Ne mogu odrediti Pruferov kod nepovezanog grafa!")
