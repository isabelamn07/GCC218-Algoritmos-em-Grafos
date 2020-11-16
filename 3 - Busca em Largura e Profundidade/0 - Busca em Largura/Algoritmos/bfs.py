##  Busca em largura
import random
from math import inf

'''
Pseudocodigo
BFS(G, s)
for each vertex u E G.V - {s}
    u.color = WHITE
    u.d = inf
    u.pi = NIL
s.color = GRAY
s.d = 0
s.pi = NIL
Q = Vazio
ENQUEUE(Q, s)
while Q != Vazio
    u = DEQUEUE(Q)
    for each v E G.Adj[u]
        if v.color == WHITE
            V.color == GRAY
            v.d = u.d +1
            u.pi = u 
            ENQUEUE(Q, v)

    u.color = BLACK
'''

'''
G - Grafo
s - vértice inicial


'''
# Lista que contém os vértices a serem explorados
Q = []
# Lista que ira conter os dados da busca em largura:
# [[vertice, cor, grau de visitacao a partir de s, pai]]
grafo_bfs = []
def bfs(Grafo, start):
    '''
    Função BFS - realiza a busca em largura de um grafo dado
    Parametros
        Grafo 
        start 
            vertice inicial
    '''
    # conjunto de vertices recebe uma lista com todos os vertices contidos
    # no grafo
    conjunto_vertices = list(Grafo.keys())
    # print('conjunto_vertices', conjunto_vertices)
    # Inicializacao de todos os vertices 
    for i in conjunto_vertices:
        grafo_bfs.append([i, 'WHITE', inf, None])

    #print('grafo_bfs', grafo_bfs)

    for j in range(len(grafo_bfs)):
        # se o vertice inicial start estiver no grafo, ele recebe:
        # grau 0
        # pai : None
        # cor: CINZA
        if start == grafo_bfs[j][0]:
            grafo_bfs[j][1] = 'GRAY'
            grafo_bfs[j][2] = 0
            grafo_bfs[j][3] = None
            j = len(grafo_bfs)   
    # A fila recebe o vertice inicial
    Q.append(start)
    while(len(Q) > 0):
        # U recebe a primeira posicao da fila
        u = Q.pop(0)
        #print("Fila de prioridade", Q)

        ## procura o indice do vertice u em grafo_bfs
        for i in range(len(grafo_bfs)):
            if grafo_bfs[i][0] == u:
                indice = i
        # se o grafo ainda nao foi explorado, recebe os valores: CINZA, o grau de distância de s e o vértice pai
        for i in Grafo[u]:                 
            if (grafo_bfs[indice_adj(conjunto_vertices, i)][1] == 'WHITE'):
                grafo_bfs[indice_adj(conjunto_vertices, i)][1] = 'GRAY'
                grafo_bfs[indice_adj(conjunto_vertices, i)
                          ][2] = grafo_bfs[indice][2] + 1
                grafo_bfs[indice_adj(conjunto_vertices, i)][3] = u
                Q.append(i)
       
        # Após ser explorado e visitado o vértice não será mais acioanado, então 
        # recebe o status PRETO. 
        for i in range(len(grafo_bfs)):
            if u == grafo_bfs[i][0]:
                grafo_bfs[i][1] = 'BLACK'

def indice_adj(vertices, x):
    '''
    Função para encontrar o índice de um vértice no grafo

    '''
    if x in vertices:
        return vertices.index(x)
  

lista_adj = {
    1: {2: 4, 5: 9, 6: 8},
    2: {1: 4, 3: 6, 4: 6, 7: 12},
    3: {2: 6, 6: 23, 5: 11, 7: 55},
    4: {2: 6, 5: 99, 6: 46, 7: 19},
    5: {1: 9, 3: 11, 4: 99},
    6: {1: 8, 3: 23, 4: 46, 10: 9},
    7: {2: 12, 3: 55, 4: 19},
    8: {9: 4},
    9: {8: 4},
    10: {6: 9}
}

bfs(lista_adj, random.choice(list(lista_adj.keys())))
print('grafo_bfs', grafo_bfs)
