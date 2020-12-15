"""
    GENERIC-MST(G, w)
    1 A = vazio
    2 while A does not form a spanning tree
    3   find an edge(u, v) that is safe for A
    4   A = A U {(u, v)}
    5 return A

    MST-Kruskal(G, w)
    A = vazio
    for each vertex v E G.v
        MAKE-SET(v)
    sort the edges of G.E into nondecreasing order by weight w
    for each edge(u, v) E G.E, taken in nondecreasing order by weight
        if FIND-SET(u) != FIND-SET(v)
            A = A U {(u, v)}
            UNION(u, v)
    return A
"""
import operator

def MST_Kruskal(Grafo):
    # lista com todas a arestas do grafo
    edges = []
    for i, j in Grafo.items():
        adj = list(j)
        for k in range(len(j)):
            if (len(edges) > 0) and (adj[k], i, Grafo[i][adj[k]] ) not in edges:
                edges.append((i, adj[k], Grafo[i][adj[k]]))
            elif len(edges) == 0:
                edges.append((i, adj[k], Grafo[i][adj[k]]))
    print(edges)
    agm = []
    # ordena as arestas em ordem crescente
    edges.sort(key=operator.itemgetter(2)) 
    #print("Edges: ", edges)
    # recebe os sets
    sets = set()
    lista_de_sets = []
    for v in Grafo.keys():        
        sets = {v}
        lista_de_sets.append(sets)
    #print("lista_de_sets", lista_de_sets)

    for w in range(len(edges)): # De acordo com a ordem crescente das arestas u e v recebem os vertices correspondentes
        for j in range(len(edges[w])):
            u = edges[w][0]
            v = edges[w][1]


        x = find_set(lista_de_sets, u) # x recebe o indice do set onde u esta inserido
        y = find_set(lista_de_sets, v) # y recebe o indice do set onde y esta inserido

        if x != y: # se u e v estiverem sets diferentes, fazemos a uniao entre eles
            agm.append((u, v))
            new_set = lista_de_sets[x].union(lista_de_sets[y])
     
            lista_de_sets.append(new_set)
            if y > x:
                lista_de_sets.pop(y)
                lista_de_sets.pop(x)
            else:
                lista_de_sets.pop(x)
                lista_de_sets.pop(y)
       
    print("AGM: ", agm)   
    print("Lista de sets: ", lista_de_sets)

def find_set(lista, x):
    '''
    Funcao que encontra o indice de um set na lista lista_de_sets
    '''
    for i in range(len(lista)):
        if x in lista[i]:
            return i
           


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

MST_Kruskal(lista_adj)
