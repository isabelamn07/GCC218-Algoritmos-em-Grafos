## DFS
#import networkx as nx
#import matplotlib.pyplot as plt
'''
DFS(G):
    for each vertex u E G.V
        u.color = WHITE
        u.pi = NIL
    time = 0
    for each vertex u E G.V
        if u.color == WHITE
            DFS-Visit(G,u)
    
    DFS-Visit(G, u):
        time = time + 1
        u.d = time
        u.color = GRAY
        for each v E G.Adj[u]
            if v.color == WHITE 
                v.pi = u
                DFS-Visit(G, v)
        u.color = BLACK
        time = time + 1
        u.f = time

G.V - conjunto de vértices
pi - vértice pai
d - tempo de descoberta
f - tempo em que o vértice é fechado, torna-se preto e não é mais explorado
'''
# variável com o controle de tempo de descoberta e fechamento do vértice
tempo = 0
# lista que contém o status de cada vértice (Branco, Cinza, Preto), assim como o vértice pai e o tempo
grafo_dfs = []
# lista que contém os vértices que já foram visitados
visitado = []

def DFS(Grafo):
    '''
    Função para inicializar os valores como: cor, pai, tempo
    Parâmetros:
        Grafo
            grafo a ser percorrido pela busca em profundidade
    '''
    # Inicialização de valores
    for i in list(Grafo.keys()):
        grafo_dfs.append([i, 'BRANCO', None])
    global tempo
    tempo = 0
    
    # percorre o conjunto de vértices
    for i in range(len(list(Grafo.keys()))):
        # caso o vertice nao tenha sido visitado, e realizada a busca em profundidade(teste para todos os vertices)
        if grafo_dfs[i][0] not in visitado:
            DFS_Visit(Grafo, grafo_dfs[i][0])


def DFS_Visit(Grafo, u):
    '''
    Função que realiza a busca em profundidade em cada ciclo/floresta de todos os vértices alcançaveis a partir de u.
        Parâmetros:
            Grafo
                Grafo a ser percorrido
            u
                vértice inicial não visitado
    '''
    # tempo de descoberta do vértice
    global tempo
    tempo += 1    
    
    # encontrando o indice do vertice u no grafo_dfs
    for i in range(len(grafo_dfs)):
        if grafo_dfs[i][0] == u:
            indice = i

    # O vértice sendo explorado, recebe a cor cinza, o tempo de descoberta
    grafo_dfs[indice][1] = 'CINZA'
    grafo_dfs[indice].append(("tempo de descoberta:", tempo))
    visitado.append(grafo_dfs[indice][0])
    #print("visitado: ", visitado)
    
    # variavel que recebera o indice do proximo vertice a ser visitado
    ind = 0
    # buscamos vertices adjacentes a u que nao tenham sido visitados ainda (BRANCOS)
    for v in Grafo[u]:        
        for i in range(len(grafo_dfs)):
            if v == grafo_dfs[i][0] and v not in visitado:
                ind = i
             
        # Ao encontrar vertices adjacentes nao visitados, continuamos a busca recursivamente  
        if grafo_dfs[ind][1] == 'BRANCO':
            grafo_dfs[ind][2] = u
            DFS_Visit(Grafo, v)
    # Ao nao ter mais vertice para explorar o vertice e fechado (torna-se preto) e recebe o tempo em que 
    # foi fechado
    for i in range(len(grafo_dfs)):
        if grafo_dfs[i][0] == u:
            grafo_dfs[i][1] = 'BLACK'
            tempo += 1
            grafo_dfs[i].append(('tempo2:' , tempo))
   
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
'''
#NetworkX
Grafo = nx.Graph()
edges = []
for i, j in lista_adj.items():
    adj = list(j)
    for k in range(len(j)):
        edges.append((i,adj[k]))

Grafo.add_nodes_from(lista_adj.keys())
Grafo.add_edges_from(edges)

nx.draw(Grafo, with_labels=True, font_weight='bold')
plt.show()
'''
DFS(lista_adj)
for i in grafo_dfs:
    print("grafo:", i)

