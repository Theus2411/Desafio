from utils.calculos import calcular_sistema, calcular_sistema_3x3
import numpy as np

A = np.array([[2, 3], [4, -1]])
B = np.array([8, 7])


det = np.linalg.det(A)
print(f"Determinante de A: {det}")

resultado = calcular_sistema(A, B)
print(f"Resultado de X: {resultado[0]}")
print(f"Resultado de Y: {resultado[1]}")

print("\nVerificação:")
print(f"2x + 3y = 2({resultado[0]:.2f}) + 3({resultado[1]:.2f}) = {2*resultado[0] + 3*resultado[1]:.2f}")
print(f"4x - y = 4({resultado[0]:.2f}) - {resultado[1]:.2f} = {4*resultado[0] - resultado[1]:.2f}")

print("--------------------------------------------------------")

# Define a matriz dos coeficientes A e o vetor B
A = np.array([[2, 1, 2], [1, 2, 3], [3, 1, 4]])
B = np.array([7, 7, 11])
# Verifica o determinante para garantir que A é invertível
det = np.linalg.det(A)
print(f"Determinante de A: {det:.2f}")

resultado = calcular_sistema_3x3(A, B)

# Exibe a solução
print("\nTaxas   de produção:")
print(f"x = {resultado[0]:.2f} itens por trabalhador")
print(f"y = {resultado[1]:.2f} itens por máquina")
print(f"z = {resultado[2]:.2f} itens por hora")
# Calcula produção com 4 trabalhadores, 2 máquinas e 3 horas
producao = 4 * resultado[0] + 2 * resultado[1] + 3 * resultado[2]
print(f"\nProdução com 4 trabalhadores, 2 máquinas e 3 horas:{producao:.2f} itens")

print("\nVerificação:")
print(f"2x + y + 2z = 2({resultado[0]:.2f}) + {resultado[1]:.2f} + 2({resultado[2]:.2f}) = {2*resultado[0] + resultado[1] +2*resultado[2]:.2f}")
print(f"x + 2y +3z = {resultado[0]:.2f} + 2({resultado[1]:.2f}) + 3({resultado[2]:.2f}) = {resultado[0] + 2*resultado[1] +3*resultado[2]:.2f}")
print(f"3x + y + 4z = 3({resultado[0]:.2f}) + {resultado[1]:.2f} + 4({resultado[2]:.2f}) = {3*resultado[0] + resultado[1] +4*resultado[2]:.2f}")