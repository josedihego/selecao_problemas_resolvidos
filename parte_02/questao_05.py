import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming

matriz_distancias = np.array([
    [0,5,4,10],
    [5,0,8,5],
    [4,8,0,3],
    [10,5,3,0]
])

caminho, distacia = solve_tsp_dynamic_programming(matriz_distancias)
print('Melhor caminho é: ', caminho)
print('Menor distância do caminho: ', distacia)