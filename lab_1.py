# Prva laboratorijska vježba, Diskretna matematika
import math
# unos podataka
n = -1
while (n < 0):
    n = int(input("Unesite nenegativan cijeli broj: "))
b_0 = float(input("Unesite vrijednost broja b_0: "))
b_1 = float(input("Unesite vrijednost broja b_1: "))
b_2 = float(input("Unesite vrijednost broja b_2: "))
c_0 = float(input("Unesite vrijednost broja c_0: "))
c_1 = float(input("Unesite vrijednost broja c_1: "))
c_2 = float(input("Unesite vrijednost broja c_2: "))

# rješavanje sustava linearnih jednadžbi (Cramerovo pravilo)
d = b_0 * c_1 - c_0 * b_1
d1 = b_2 * c_1 - c_2 * b_1
d2 = b_0 * c_2 - c_0 * b_2
lambda_1 = d2 / d
lambda_2 = d1 / d

# izračun
det = pow(lambda_1, 2) + 4 * lambda_2

if (det == 0):
    x = lambda_1 / 2
    l1 = b_0
    l2 = b_1 / x - b_0
    b_n = l1 * pow(x, n) + l2 * n * pow(x, n)
else:
    if (det > 0):
        x1 = (lambda_1 + math.sqrt(det)) / 2
        x2 = (lambda_1 - math.sqrt(det)) / 2
    else:
        x1 = complex(lambda_1/2, math.sqrt(abs(det))/2)
        x2 = complex(lambda_1/2, - math.sqrt(abs(det))/2)
    l2 = (b_1 - b_0 * x1) / (x2-x1)
    l1 = b_0 - l2
    b_n = (l1 * pow(x1, n) + l2 * pow(x2, n)).real

print("Vrijednost broja b_n:", round(b_n, 2))
