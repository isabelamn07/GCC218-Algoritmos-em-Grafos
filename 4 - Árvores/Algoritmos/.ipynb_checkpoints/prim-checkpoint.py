from math import inf
import sys
import random

# Grafo no formato de matriz de adjacência
grafo = [[0, 4, 0, 0, 9, 8, 0, 0, 0, 0],
         [4, 0, 6, 6, 0, 0, 12, 0, 0, 0],
         [0, 6, 0, 0, 11, 23, 55, 0, 0, 0],
         [0, 6, 0, 0, 99, 46, 19, 0, 0, 0],
         [9, 0, 11, 99, 0, 0, 0, 0, 0, 0],
         [8, 0, 23, 46, 0, 0, 0, 0, 0, 9],
         [0, 12, 55, 19, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 4, 0],
         [0, 0, 0, 0, 0, 0, 0, 4, 0, 0],
         [0, 0, 0, 0, 0, 9, 0, 0, 0, 0]]


# lista com vertices já visitados
visitado = []

def MST_PRIM(G, vertice_inicial):
    '''
    A função MST_PRIM encontra a árvore geradora mínima em um grafo, representado por uma matriz de adjacência NxN,
    ao receber um vértice inicial r, calcula as distâncias dos vértices mais próximos, adjacentes a r. As arestas não se 
    repetem e o devem gerar uma árvore(sem ciclos) com todas as arestas de menor peso do grafo.
    Parametros:
        G
            matriz de adjacência represtando o grafo
            
        vertice_inicial   
            vértice inicial
    '''

    # Matriz que recebe as arestas (u, v) de menor peso
    # forma [u, peso, v]
    matriz_prim = []
    for i in range(len(G)):
        # inicialmente a matriz recebe todos os vértices: u, distância(peso): infinito, vértice v: None
        matriz_prim.append([i, inf, None])

    # O vertice inicial nao tem pai por isso recebe distancia 0    
    matriz_prim[vertice_inicial][1] = 0
    print("Vertice inicial", vertice_inicial)
    # Q recebe todos os vertices do grafo
    Q = []
    for i in range(len(matriz_prim)):
        Q.append(i)
    # enquanto toda a arvore nao for percorrida, ou seja,
    # enquanto todos os vertices forem visitados, o programa
    # continua procurando as arestas de menor peso
    while len(Q) > 0:
        if len(visitado) == 0:
            # recebe o vertice inicial passado por parametro
            u = vertice_inicial
            Q.remove(u)
            visitado.append(u)
        else:
            # u recebe o vizinho mais proximo dentre os vertices ja vistados
            u = extract_min(Q)
            visitado.append(u)
            print("Q", Q)
            Q.remove(u)

        # percorre a matriz com as distancia dos vertices e atualiza
        # sempre que encontrar distancias menores
        for v in range(len(G)):
            if G[u][v] < matriz_prim[v][1] and G[u][v] != 0 and v in Q:
                matriz_prim[v][2] = u
                matriz_prim[v][1] = G[u][v]

    print("lista: ", matriz_prim)

def extract_min(Q):
    # indices da matriz que vao receber a menor aresta
    # e o vizinho mais proximo
    linha = 0
    coluna = 0
    # valor muito grande para fazer comparacoes e achar o menor valor
    menor = inf        
    # percore na matriz os vertices adjacentes ao vertices ja visitados
    # e encontra o vizinho mais proximo
    v = None
    print("Vertices visitados: ", visitado)
    for i in visitado:
        for j in range(len(grafo[i])):
            if j not in visitado and grafo[i][j] != 0:
                if grafo[i][j] < menor:
                    menor = grafo[i][j]
                    u = i
                    v = j

    # nosso exemplo tem um grafo desconexo, ao procurar as menores arestas
    # dentre os vertices visitados chegamos em um ponto onde Q ainda tem 
    # vertices nao visitados, porem esses vertices a serem explorados
    # nao sao alcancaveis a partir de nenhum dos vertices ja visitados,
    # portanto precisamos retornar v a partir da estrutura Q que possui
    # os vertices nao visitados
    if v == None:
        v = random.choice(Q)
        
    return v

u = random.randrange(0, len(grafo))
MST_PRIM(grafo, u)