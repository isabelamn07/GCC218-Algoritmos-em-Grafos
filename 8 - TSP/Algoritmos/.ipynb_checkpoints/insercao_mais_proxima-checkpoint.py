# Pseudocódigo
'''
1 Selecione um par de vértices
2 Crie um ciclo indo do primeiro vértice ao segundo e voltando ao primeiro
3 Enquanto houver vértices não visitados:
3.1 Para todo vértice não visitado:
3.1.1 Encontre a posição no ciclo atual onde a visita do vértice provoca o menor aumento no custo total no ciclo
3.2 Encontre o vértice não visitado tal que o aumento calculado no passo 3.1.1 é o menor dentre todos os vértices 
não visitados
3.3 Insira-o na posição correspondente do ciclo
'''
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

x = grafo[:] # copia do grafo

def insercao_tsp():
    visitado = [] # guarda vertics ja visitados
    if grafo:
        v1 = random.randint(0, len(grafo))
        print("V1 ", v1)
        visitado.append(v1)
        caminho.append(v1)
        for i in range(len(x)):
            x[i][i] = inf
            x[i][v1] = inf
        print(x)
        print(caminho)
        while len(visitado) < len(grafo):
            i, j = find_min(visitado)
            visitado.append(j)
            tsp_insert()
            for i in range(len(x)):
                x[i][j] = inf
                x[i][j] = inf
        caminho.append(v1)
    print(caminho)
    print(visitado)

def find_min(visitado):
    menor = inf
    coluna = 0
    linha = 0
    for i in visitado:
        for j in range(len(x)):
            if  x[i][j] < menor:
                menor = x[i][j]
                linha = i
                coluna = j
    print(linha, coluna)
    return linha, coluna

def tsp_insert():
    pass


        

insercao_tsp()
