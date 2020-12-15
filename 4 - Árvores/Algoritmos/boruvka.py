# Boruvka

from math import inf

lista_adj = {
    0: {1: 4, 7: 8},
    1: {0: 4, 2: 8, 7: 11},
    2: {1: 8, 5: 4, 3: 7, 8: 2},
    3: {2: 7, 4: 9, 5: 14},
    4: {3: 9, 5: 10},
    5: {2: 4, 3: 14, 4: 10, 6: 2},
    6: {5: 2, 7: 1, 8: 6},
    7: {0: 8, 1: 11, 6: 1, 8: 7},
    8: {2: 2, 6: 6, 7: 7}

}

# Recebe todas as arestas do grafo
grafo_boruvka = []
# Recebe as arestas que formam a AGM
arvore = []


def boruvka_agm():
    '''
    Função 
    '''
    # Cria um set para cada vértice
    sets = [set([x]) for x in lista_adj.keys()]

    # Atribui à lista grafo_boruvka as arestas do grafo
    for i in lista_adj.keys():
        for j in lista_adj[i]:
            grafo_boruvka.append((i, j))

    #print("grafo boruvka", grafo_boruvka)
    # Enquanto existir mais de um set continuamos a unir os componentes para gerar a AGM
    while(len(sets) > 1):
        #print("sets", sets)
        itera = sets[:] # criamos um set auxiliar para modificar a lista sets
        for i in range(len(itera)): # o tamanho de sets não pode ser modificado durante a iteracao do loop for
            edge = find_sets(itera[i], grafo_boruvka)
            arvore.append(edge)
            uniao_sets(edge, sets)
    print(sets)


def find_sets(u, grafo):
    '''
    Função para encontrar o menor valor de conexao entre os sets
    Parametros
        u
            set atual
        grafo
            lista com todas as arestas do grafo(grafo_boruvka)
    '''
    print("u", u)
    
    menor_valor = inf
    # econtra o menor peso dentre os sets adjacentes
    for x in u:
        for i in lista_adj[x]:
            if (x, i) in grafo:
                if lista_adj[x][i] < menor_valor:
                    menor_valor = lista_adj[x][i]
                    edge = (x, i)
    if edge in grafo:
        grafo_boruvka.remove(edge)
    print(edge, "edge")
    return edge


def uniao_sets(set1, sets):
    '''
    Função para unir os sets
    '''
    indices = []
    for i in range(len(sets)):
        if set1[0] in sets[i]:
            indices.append(i)
        if set1[1] in sets[i]:
            indices.append(i)
    if len(indices) == 2:
        if indices[0] != indices[1]:
            componente = set.union(sets[indices[0]], sets[indices[1]])
            sets.append(componente)

        if indices[0] > indices[1]:
            sets.pop(indices[0])
            sets.pop(indices[1])
        elif indices[0] < indices[1]:
            sets.pop(indices[1])
            sets.pop(indices[0])


boruvka_agm()
print(arvore)
