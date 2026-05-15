import numpy as np

from utils.calculos import calcular_sistema_3x3

A = np.array([[1, 2, -1], [2, -1, 2], [3, 1, 1]])
B = np.array([3, 7, 8])

print(np.linalg.solve(A, B))