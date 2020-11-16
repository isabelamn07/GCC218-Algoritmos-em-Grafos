import random

# lista de adjacencia de um grafo nao bipartido

grafo = {
    1: {2: 4, 5: 9, 6: 8},
    2: {1: 4, 3: 6, 4: 6, 7: 2},
    3: {2: 6, 6: 23, 5: 11, 7: 55},
    4: {2: 6, 5: 99, 6: 46, 7: 19},
    5: {1: 9, 3: 11, 4: 99},
    6: {1: 8, 3: 23, 4: 46, 10: 9},
    7: {2: 7, 3: 55, 4: 19},
    10: {6: 9}
}

'''
# lista de adjacencia de um grafo bipartido
grafo = { 1: {2:0, 3:0},
          2: {1:0, 4:0},
          3: {1:0, 4:0},
          4: {2:0, 3:0}

}
'''


def DFS(Grafo, s, visitado, cores):
    '''
    Para determinar se o grafo é bipartido ou nao, fazemos um busca, aqui usamos a busca em profundidade 
    e verificamos se o grafo é 2-colorível, atribuindo um valor 0 representando uma cor para um vértice 
    por exemplo e todos seus adjacentes com um cor diferente representada aqui pelo número 1. Caso núme-
    ros iguais não estejam conectados(adjacentes) o grafo é bipartido.
    '''
    if s not in visitado:
        visitado.append(s)
        # atribuimos 0 para cada vértice do grafo como forma de inicializacao da lista
        for i in range(len(Grafo.keys())):
            cores.append(0)

    # percorremos o grafo (DFS)
    for v in Grafo[s]:
        if v not in visitado:
            visitado.append(v)
            # indices dos vertices adjacentes (v)
            indice = list(Grafo.keys()).index(v)
            # indice do vertice que esta sendo visitado (u)
            indice1 = list(Grafo.keys()).index(s)
            
            # atribuimos valores para cada vertice, se o valor atribuido a um vertice na lista cores for 1
            # atribuimos 0 aos adjacentes e vice versa.
            if cores[indice1] == 0:
                cores[indice] = 1
            elif cores[indice1] == 1:
                cores[indice] = 0
            # caso o grafo seja vazio, retorna falso
            if (not DFS(Grafo, v, visitado, cores)):
                return False
        # se dois vertices adjacentes (s, v) tem o mesmo valor, entao o grafo nao e bipartido
        elif (cores[list(Grafo.keys()).index(s)] == cores[list(Grafo.keys()).index(v)]):
            return False
    return True


# guarda os vertices ja visitados
visitado = []
# contem as cores de todos os vertices, essas cores sao representadas por 0 ou 1
cores = []
eh_bipartido = DFS(grafo, random.choice(list(grafo.keys())), visitado, cores)
if eh_bipartido:
    print("O grafo e bipartido")
else:
    print("O grafo nao e bipartido")

