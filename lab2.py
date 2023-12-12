def checkHamilton(matrix, v, visited, path):

    # ako ima hamiltonovski put
    if (len(path) == n and matrix[0][path[-1]] == 1):
        return True

    for u in range(n):  # provjera za svaki vrh
        if (matrix[v][u] == 1):  # ako su povezani
            if (visited[u] == False):
                visited[u] = True
                path.append(u)  # dodaj u put

                if (checkHamilton(matrix, u, visited, path)):
                    return True
                # ako nema puta s ovim vrhom na ovoj poziciji
                visited[u] = False
                path.pop()  # izbaci ga
    return False


def checkConnection(matrix, v, visited, path):
    if (len(path) == n):  # ako smo prošli sve vrhove, povezan je
        return True
    for u in range(n):
        if (matrix[v][u] == 1):
            if (visited[u] == False):  # ako ga još nismo posjetili
                path.append(u)
                visited[u] = True
                if (checkConnection(matrix, u, visited, path)):
                    return True
    return False


# ulazni podaci
n = int(input("Unesite prirodan broj n: "))
k_1 = int(input("Unesite vrijednost prirodnog broja k_1: "))
k_2 = int(input("Unesite vrijednost prirodnog broja k_2: "))
k_3 = int(input("Unesite vrijednost prirodnog broja k_3: "))
k_4 = int(input("Unesite vrijednost prirodnog broja k_4: "))

# matrica susjedstva
matrix = []
for i in range(n):
    m = []
    for j in range(n):
        if (i != j):
            if (abs(i-j) == k_1 or abs(i-j) == k_2 or abs(i-j) == k_3 or abs(i-j) == k_4):
                m.append(1)
            else:
                m.append(0)
        else:
            m.append(0)
    matrix.append(m)

# provjerava povezanost
connected = True

visited = [False]*n
visited[0] = True
path = [0]
connected = checkConnection(matrix, 0, visited, path)

print("Graf G je povezan graf" if connected else "Graf G nije povezan graf")

# provjerava je li graf hamiltonovski
hamilton = False

if (connected):
    if (n == 1 or n == 2):
        pass
    else:
        visited = [False] * n
        path = [0]
        visited[0] = True
        hamilton = checkHamilton(matrix, 0, visited, path)

# ispis rješenja
print("Graf G je hamiltonovski graf" if hamilton else "Graf G nije hamiltonovski graf")
