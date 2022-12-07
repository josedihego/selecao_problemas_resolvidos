import random
import numpy as np
tamanho = 5

matriz = [0] * tamanho

for i in range(tamanho):
    matriz[i] = [0] * tamanho

for i in range(tamanho):
    for j in range(tamanho):
        matriz[i][j] = random.randint(0,20)

linhas_mesma_soma =  True
soma_linha = sum(matriz[0])
for i in range(1,tamanho):
    soma = sum(matriz[i])
    if(soma!=soma_linha):
        linhas_mesma_soma = False
        break

np.transpose(matriz)

colunas_mesma_soma =  True
soma_coluna = sum(matriz[0])
for i in range(1,tamanho):
    soma = sum(matriz[i])
    if(soma!=soma_coluna):
        colunas_mesma_soma = False
        break

np.transpose(matriz)
