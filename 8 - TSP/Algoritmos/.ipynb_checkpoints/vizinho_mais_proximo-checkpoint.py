
import random
import sys
from math import inf
# Grafo no formato de matriz de adjacência
grafo = [[0, 7, 1, 15, 8, 3],
         [7, 0, 9, 21, 5, 4],
         [1, 9, 0, 35, 26, 12],
         [15, 21, 35, 0, 13, 42],
         [8, 5, 26, 13, 0, 5],
         [3, 4, 12, 42, 5, 0]]

caminho = []

def vizinho_tsp():
    
    if grafo:
        v1 = random.randint(0, len(grafo)-1)
        caminho.append(v1)
        for i in range(len(grafo)):
            grafo[i][i] = inf
        while len(caminho) < len(grafo):
            j = find_min()
            caminho.append(j)
    caminho.append(caminho[0])  
    print("Caminho", caminho)

def find_min():
    menor = inf
    coluna = 0
    linha = 0
    for i in caminho:
        for j in range(len(grafo)):
            if  (grafo[i][j] < menor) and j not in caminho:
                menor = grafo[i][j]
                linha = i
                coluna = j
   
    return coluna

vizinho_tsp()
