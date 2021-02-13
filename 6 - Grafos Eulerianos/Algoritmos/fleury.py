import random
from math import inf

#Grafo G
grafo = { 'A': {'B': 0, 'C': 0, 'D': 0, 'E': 0},
          'B': {'A': 0, 'C': 0, 'D': 0, 'E': 0},
          'C': {'A': 0, 'B': 0, 'D': 0, 'E': 0},
          'D': {'A': 0, 'B': 0, 'C': 0, 'E': 0},
          'E': {'A': 0, 'B': 0, 'C': 0, 'D': 0}
        }


indices = {} #Dicionario com os indices de cada vertice no grafo
count = 0
for i in grafo:
    indices.update({i: count})
    count += 1

def verifica_graus():
    '''
    Verifica se o grafo possui todos vértices com grau par ou apenas dois vertices com grau impar que e
    a condicao para um grafo possuir um trilha euleriana ou ser euleriano
    '''
    vertices_grau_impar = []
    vertices = []
    for i, j in grafo.items():
        vertices.append(i)
        if (len(j) % 2 == 1):
            vertices_grau_impar.append(i)

    if (not(vertices_grau_impar)):
        return vertices
    elif (len(vertices_grau_impar) == 2):
        return vertices_grau_impar
    else:
        return False

def fleury_func(v):
    '''
    Função que percorre o grafo, deleta arestas incluidas na trilha euleriana e vertices isolados
    Parametros
        v
            Vertice inicial, set todos os graus dos vertices no grafo forem pares, escolhe aleatoriamente
            senao, recebe um vertice de grau impar
    '''
    caminho = [] # caminho percorrido
    arestas = {} # Dicionario que possui todas as arestas do grafo marcadas com False 

    for i in grafo.keys():
        for j in grafo[i]:
            if (j, i) not in arestas:
                arestas.update({(i, j) : False})
   
    total_arestas_marcadas = 0 # contador para verificar quantas arestas foram marcadas
    
    while total_arestas_marcadas < len(arestas): # quando todas arestas forem marcadas significa que todas ja foram percorridas uma vez
        w = None      
        pontes = [] # lista de arestas que sao pontes a partir do vertice v
        arestas_possiveis = [] # lista com todas as aresta a partir de v
        for aresta in arestas:
            if v in aresta and not arestas[aresta]:
                arestas_possiveis.append(aresta)

        while len(arestas_possiveis) > 0: # a partir de v escolhemos uma aresta para atravessar evitando pontes
            aresta = random.choice(arestas_possiveis) # as arestas sao escolhidas aleatoriamente
            if aresta[0] == v:
                k = aresta[1]
            else:
                k = aresta[0]
            if(detecta_ponte(v, k) == False and w is None): # ao escolher uma aresta que nao e uma ponte a atravessamos
                w = k # w recebe o valor do vertice de destino a partir de v quando nao escolhemos uma ponte
                if (v, k) in arestas:
                    arestas[(v, k)] = True
                    total_arestas_marcadas += 1
                else:
                    arestas[k, v] = True
                    total_arestas_marcadas += 1
                arestas_possiveis.clear()
            elif(detecta_ponte(v, k) == True): # tentamos evitar as pontes, mas caso elas sejam escolhidas na lista de arestas possiveis
                # as guardamos em uma lista e somente caso nao haja outra alternativa, escolhemos uma ponte para atravessar
                pontes.append(k)
                if (v, k) in arestas_possiveis:
                    arestas_possiveis.remove((v, k))
                else:
                    arestas_possiveis.remove((k, v))

        print(pontes)
        if(not w): # w fica vazio se so encontrarmos pontes a partir de v
            w = random.choice(pontes) # como nao temos mais outras alternativas escolhemos uma ponte para atravessar
            if (v, w) in arestas:
                arestas[(v, w)] = True
                total_arestas_marcadas += 1
            else:
                arestas[w, v] = True
                total_arestas_marcadas += 1
        if w:
            caminho.append((v, w)) # deletamos as arestas ja percorridas do grafo
            del grafo[w][v]
            del grafo[v][w]
            if( grafo[v] == {}): # deletamos vertices isolados
                del grafo[v]
            if grafo[w] == {}: # se o grafo estiver vazio e deletado
                del grafo[w]
            if (len(grafo) > 0):
                v = w  # ao atravessar uma aresta o vertice w se torna v 
    
    return caminho


descoberta = [inf] * (len(grafo)) # guarda o tempo de descoberta do vertice (busca em profundidade)
low = [inf] * (len(grafo))  # guarda o menor vertice alcançavel por um vertice v
pais = [-999] * (len(grafo)) # recebe um caminho de vertices e seus respectivos pais 
visitado = []

def encontra_pontes(v, tempo):
    print(visitado)
    '''
    Funcao que encontra pontes no grafo, usando busca em profundidade
    '''
    lista_pontes = [] 

    if grafo: # se o grafo nao estiver vazio
        visitado.append(v) 
        descoberta[indices[v]] = tempo
        low[indices[v]] = tempo
        tempo += 1
        for w in grafo[v]:
            if w not in visitado:
                pais[indices[w]] = v
                encontra_pontes(w, tempo)
                low[indices[v]] = min(low[indices[v]], low[indices[w]]) # recebe o menor vertice que v pode alcancar

                if low[indices[w]] > descoberta[indices[v]]: # se o menor vertice alcancavel 
                    # se v for maior que o tempo de descoberta do vertice v, temos uma ponte
                    lista_pontes.append((v, w))

            elif w != pais[indices[v]]:
                    low[indices[v]] = min(
                        low[indices[v]], descoberta[indices[w]])
        return lista_pontes

def detecta_ponte(v, i):
    '''
    Retorna True caso um aresta seja uma ponte e False caso contrário
    Parametros
        v
            vertice de origem v
        i 
            vertice de destino i
            
    '''

    tempo = 0   
    visitado.clear()
    lista_pontes = encontra_pontes(v, tempo)
    if (v, i) in lista_pontes:
        return True
    else:
        return False

V = verifica_graus()
if (V != False):
    vertice_inicial = random.choice(V)
    caminho_percorrido = fleury_func(vertice_inicial)
    print(caminho_percorrido)
else:
    print("O grafo não é Euleriano, nem possui trilha euleriana")

