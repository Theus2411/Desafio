import numpy as np

from utils.calculos import calcular_sistema_3x3

print("Digite os coeficientes de A:")
A = [[None] * 3 for _ in range(3)]
for linha, item in enumerate(A):
    for coluna, item2 in enumerate(item):
        A[linha][coluna] = float(input(f"A:[{linha}][{coluna}]:"))

print("Digite os termos independentes (B):")
B = [None]*3
for linha, item in enumerate(B):
        B[linha] = float(input(f"B:[{linha}]: "))


print("Matriz A: ")
for item in A:
    print(f"{item[0]: .0f} {item[1]: .0f} {item[2]: .0f}")

print("Matriz B: ")
print(B)

A = np.array(A)
B = np.array(B)

resultado = calcular_sistema_3x3(A, B)
print(f"x = {resultado[0]: .2f}")
print(f"y = {resultado[1]: .2f}")
print(f"z = {resultado[2]: .2f}")


