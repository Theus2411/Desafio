import numpy as np

def calcular_sistema(A, B):
    try:
        A_inversa = np.linalg.inv(A)
        X = np.dot(A_inversa, B)
        return X
    except np.linalg.LinAlgError:
        print("Erro matriz nao invertivel:")


def calcular_sistema_3x3(A, B):
    try:
        if np.abs(np.linalg.det(A)) < 1e-10:  # Determinante próximo de zero
            print("Erro: matriz não invertível.")

        else:
            # Resolve o sistema
            X = np.linalg.solve(A, B)
            return X

    except np.linalg.LinAlgError:
        print("Erro: matriz não invertível.")
        return None