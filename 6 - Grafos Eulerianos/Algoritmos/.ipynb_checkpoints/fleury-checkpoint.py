import random
from math import remainder
import copy
from math import inf

#Grafo G
grafo = {'A': {'B': 0, 'D': 0},
         'B': {'A': 0, 'C': 0, 'D': 0, 'E': 0},
         'C': {'B': 0, 'D': 0},
         'D': {'A': 0, 'B': 0, 'C': 0, 'I': 0},
         'E': {'B': 0, 'F': 0, 'G': 0, 'H': 0},
         'F': {'E': 0, 'G': 0},
         'G': {'E': 0, 'F': 0, 'H': 0, 'K': 0},
         'H': {'E': 0, 'G': 0},
         'I': {'D': 0, 'J': 0, 'L': 0, 'K': 0},
         'J': {'I': 0, 'K': 0},
         'K': {'G': 0, 'I': 0, 'J': 0, 'L': 0},
         'L': {'I': 0, 'K': 0}
         }


pontes = [] 
caminho = []
visitado = [] # guarda os vertices visitado na busca realizada para encontrar pontes
descoberta = [inf] * (len(grafo)) # guarda o tempo de descoberta do vertice (busca em profundidade)
low = [inf] * (len(grafo))  # guarda o menor vertice alcançavel por um vertice u
pais = [-999] * (len(grafo)) # recebe um caminho de vertices e seus respectivos pais 
grafo_aux = {} # recebe o grafo modificado, depois das remocoes das arestas e vertices
grafo_aux = copy.deepcopy(grafo)
tempo = 0 

indices = {} #Dicionario com os indices de cada vertice no grafo
count = 0
for i in grafo:
    indices.update({i: count})
    count += 1


def fleury_func(u):
    '''
    Função que percorre o grafo, deleta arestas incluidas na trilha euleriana e vertices isolados
    Parametros
        u
            Vertice inicial, set todos os graus dos vertices no grafo forem pares, escolhe aleatoriamente
            senao, recebe um vertice de grau impar
    '''
    global grafo_aux
    while grafo: # Enquanto o grafo não estiver vazio, continuamos montando uma trilha
        for i in grafo_aux[u]: # itera sobre o vertices adjcente a u
            if bridge(u, i) == False and len(grafo) > 1: # se a aresta escolhida nao for uma ponte e o grafo nao for vazio
                caminho.append((u, i)) # adicionamos a aresta ao caminho
                del grafo[u][i] # deleta a aresta no grafo
                del grafo[i][u]  # deleta a aresta no grafo
                if (grafo[u] == {}): # deleta vertices isolados
                    del grafo[u]
                if (grafo[i] == {}):
                    del grafo[i]
                grafo_aux = copy.deepcopy(grafo) # usamos um vertice auxiliar para poder modificar grafo sem interferir no loop for
                fleury_func(i) # chamada recursica do vertice v da aresta (u, v)
        if grafo:
            caminho.append((u, i))
            del grafo[u][i]
            del grafo[i][u]
            if (grafo[u] == {}):
                del grafo[u]
            if (grafo[i] == {}):
                del grafo[i]
            grafo_aux = copy.deepcopy(grafo)
            fleury_func(i)

def bridges(u):
    '''
    Funcao que encontra pontes no grafo, usando busca em profundidade
    '''
    if grafo: # se o grafo nao estiver vazio
        global tempo # variavel com o tempo de descoberta dos vertices
        visitado.append(u) 
        descoberta[indices[u]] = tempo
        low[indices[u]] = tempo
        tempo += 1
        for v in grafo[u]:
            if v not in visitado:
                pais[indices[v]] = u
                bridges(v)
                low[indices[u]] = min(low[indices[u]], low[indices[v]]) # recebe o menor vertice que u pode alcancar

                if low[indices[v]] > descoberta[indices[u]]: # se o menor vertice alcancavel 
                    #por u for maior que o tempo de descoberta do vertice u, temos uma ponte
                    pontes.append((u, v))

            elif v != pais[indices[u]]:
                    low[indices[u]] = min(
                        low[indices[u]], descoberta[indices[v]])
        return pontes

def bridge(u, i):
    '''
    Retorna True caso um aresta seja uma ponte e False caso contrário
    Parametros
        u
            vertice de origem u
        i 
            vertice de destino i
            
    '''
    global tempo
    tempo = 0
    visitado.clear()
    pontes.clear()
    bridges(u)
    if (u, i) in pontes:
        return True
    else:
        return False

def start_index():
    '''
    Fucao para determinar o vertice inicial
    '''
    count = 0
    for x in grafo.keys():
        for y in grafo[x]:
            count += 1
        if remainder(count, 2) > 0:
            return x
        else:
            count = 0
    indice = random.randint(0, len(grafo)-1)
    vertices = list(grafo.keys())
    return vertices[indice]


indice = start_index()
fleury_func(indice)
print(caminho)
