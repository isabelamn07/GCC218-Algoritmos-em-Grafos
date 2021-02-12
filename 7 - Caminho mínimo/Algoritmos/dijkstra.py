from math import inf

visitado = [] # lista que recebe os vértices já visitados
single_source = [] # matriz com o caminho mínimo no formato [[vértice, distância, vértice pai], ...]

def dijkstra_cm(grafo, s):
    '''
    Função que recebe o grafo e o vértice inicial, inicializa os valores da matriz single_source
    e encontra o caminho mínimo
    Parametros:
        grafo
            grafo que procuramos o caminho mínimo
        s
            vértice inicial
    '''
    # inicialização dos valores na matriz single_source
    for i in grafo.keys():
        single_source.append([i, inf, None])
    single_source[0][1] = 0    

    Q = list(grafo.keys()) # lista que recebe o conjunto de todos os vértices
    
    # loop para encontrar o caminho mínimo visitando todos os vértices
    while len(Q) != 0: # enquanto Q não for vazio
        u = extract_min(Q) # u recebe o vértice com menor distância a partir do vértice inicial, que ainda não foi visitado
        Q.remove(u) # após visitado o vértice é removido
        visitado.append(u)
        print("Q:", Q)
        for v in grafo[u]:
            relax(u, v) # funcao que compara valores na matriz single_source para encontrar o menor caminho
    print('single source', single_source)

def extract_min(Q):
    '''
    Funcao que retorna o vertice com menor distancia atribuida que ainda nao foi visitado
    Parametros
        Q
            lista com vertices do grafo que ainda serao visitados
    '''
    menor = inf
    valor = 'x'
    for x in Q:
        if single_source[vertices.index(x)][1] < menor and x not in visitado:
            menor = single_source[vertices.index(x)][1]
            valor = single_source[vertices.index(x)][0]

    visitado.insert(0, valor)
    print('single source', single_source)
    return valor

def relax(u, v):
    '''
    Compara os valores dos caminhos encontrados com os valores de distancia atuais, caso encontre um caminho 
    com distancia menor, atualiza a matriz single_source com a nova distacia
    Parametros
        u 
            vertice do grafo
        v 
            vertice adjacente a u
    '''
    if single_source[vertices.index(v)][1] > \
            single_source[vertices.index(u)][1] + grafo[u][v]:
        single_source[vertices.index(
            v)][1] = single_source[vertices.index(u)][1] + grafo[u][v]
        single_source[vertices.index(
            v)][2] = u

# grafo no formato de lista de adjacência
grafo = {'s': {'t': 10, 'y': 5},
         't': {'x': 1, 'y': 2},
         'x': {'z': 4},
         'y': {'t':3, 'x': 9, 'z': 2},
         'z': {'s': 7, 'x': 6}
         }
vertices = list(grafo.keys())
dijkstra_cm(grafo, vertices[0])
