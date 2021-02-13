#tsp algoritmo guloso(greedy)

'''
pseudocodigo
1 Para cada aresta do grafo, em ordem nao-descrecente de custo
1.1 Se a inclusão da aresta nao deixa o grau de nenhum vertice maior do 
que 2 e nao provoca subciclos, inclua a aresta na solução'''

import operator
# Grafo no formato de matriz de adjacência
grafo = grafo = {0: {1: 7, 2: 1, 3: 15, 4: 8, 5: 3},
                 1: {0: 7, 2: 9, 3: 21, 4: 5, 5: 4},
                 2: {0: 1, 1: 9, 3: 35, 4: 26, 5: 12},
                 3: {0: 15, 1: 21, 2: 35, 4: 13, 5: 42},
                 4: {0: 8, 1: 5, 2: 26, 3: 13, 5: 5},
                 5: {0: 3, 1: 4, 2: 12, 3: 42, 4: 5}}
caminho = []
arestas = [] # estrutura que recebe todas as arestas do grafo e seus respectivos pesos


def tsp_guloso():

    grau_vertice_visitado = {} # estrutura que recebe o grau de cada vertice

    for i, j in grafo.items():
        adj = list(j)
        for k in range(len(j)):
            if (len(arestas) >= 0) and (adj[k], i, grafo[i][adj[k]]) not in arestas:
                arestas.append((i, adj[k], grafo[i][adj[k]]))

    arestas.sort(key=operator.itemgetter(2)) # ordenamos as arestas de acordo com o valor de seu peso

    print("Arestas ordenadas: ", arestas)

    for i in grafo:
        grau_vertice_visitado.update({i: 0}) 

    for aresta in arestas:
        if grau_vertice_visitado[aresta[0]] < 2 and  grau_vertice_visitado[aresta[1]] < 2: # o grau de nenhum dos vertices da aresta a ser adicionada pode ser maior ou igual a 2
            grau_vertice_visitado.update({aresta[0]: grau_vertice_visitado[aresta[0]]+1}) # atualizacao do grau dos vertices
            grau_vertice_visitado.update({aresta[1]: grau_vertice_visitado[aresta[1]]+1})
            caminho.append((aresta[0], aresta[1]))

tsp_guloso()

print('caminho', caminho)
