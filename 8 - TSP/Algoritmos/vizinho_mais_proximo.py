import random
from math import inf

# Grafo no formato de matriz de adjacência
grafo = [[0, 7, 1, 15, 8, 3],
         [7, 0, 9, 21, 5, 4],
         [1, 9, 0, 35, 26, 12],
         [15, 21, 35, 0, 13, 42],
         [8, 5, 26, 13, 0, 5],
         [3, 4, 12, 42, 5, 0]]

caminho = []

def tsp_vizino_mais_proximo():
    
    if grafo:
        v1 = random.randint(0, len(grafo)-1)# v1 recebe o primeiro vértice aleatoriamente
        caminho.append(v1) # o vértice é adicionado ao caminho

        while len(caminho) < len(grafo): # procuramos o vizinho mais proximo ate todos vertices serem adicionados ao caminho
            j = encontra_vizinho_mais_proximo()
            caminho.append(j)
            
    caminho.append(caminho[0])  
    print("Caminho", caminho)

def encontra_vizinho_mais_proximo():    
    '''
    Encontra e retorna o vizinho com a aresta incidente de menor peso a partir de todos os vértices já visitados
    '''
    menor = inf
    vertice_v = 0
    i = caminho[-1] # i recebe o ultimo vertice visitado
    for j in range(len(grafo)):
        if  (grafo[i][j] < menor) and j not in caminho and i != j: # encontramos o vizinho mais proximo que ainda nao foi visitado 
            menor = grafo[i][j]
            vertice_v = j
   
    return vertice_v

tsp_vizino_mais_proximo()
