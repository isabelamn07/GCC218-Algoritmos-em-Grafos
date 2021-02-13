import random
from math import inf
# Grafo no formato de matriz de adjacência
grafo = [[0, 7, 1, 15, 8, 3],
         [7, 0, 9, 21, 5, 4],
         [1, 9, 0, 35, 26, 12],
         [15, 21, 35, 0, 13, 42],
         [8, 5, 26, 13, 0, 5],
         [3, 4, 12, 42, 5, 0]]

ciclo = []

def insercao_tsp():
    visitado = [] # guarda vertices ja visitados
    if grafo:
        v1 = random.randint(0, len(grafo)-1) # um vertice e escolhido aleatoriamente no grafo
        visitado.append(v1)
        ciclo.append(v1) # adicionamos o vértice inicial ao ciclo
        print(grafo)
        while len(visitado) < len(grafo): # a execucao do algoritmo só encerrada quando todos os vertices forem adicionados ao ciclo
            indice, vertice_a_ser_inserido = find_min(visitado) # i recebe o indice onde o vertice v sera inserido no ciclo, e j recebe o vertice a ser inserido no ciclo
            if indice == 0: # i retorna 0 quando ha apenas o primeiro vértice no ciclo
                ciclo.extend([vertice_a_ser_inserido, ciclo[0]]) # adicionamos v ao ciclo e o vertice inicial, ja que temos que retornar ao ponto de partida.
            else:
                ciclo.insert(indice, vertice_a_ser_inserido) # inserimos a nova aresta no local que gera o menor custo
            visitado.append(vertice_a_ser_inserido)
            print("ciclo parcial:", ciclo)
    print("ciclo final:", ciclo)
    print("ordem de visitação:", visitado)

def find_min(visitado):
    '''
    Encontra a aresta de menor custo e local onde inseri-la no ciclo 
    Parametro:
        visitado
            lista que contem todos os vertices ja visitados            
    '''
    # primeiro econtramos a aresta de menor valor


    n = 0 # n representa o indice dos vertices ja visitados
    i = 0 # recebe o vertice visitado[n]
    j = 0 # recebe o vertice visitado[n+1]
    indice = 0 #retorna o indice onde o novo vertice sera introduzido no ciclo
    vertice_a_ser_inserido = 0 
    custo = 0 # recebe o resultado do calculo do custo de adicionar um novo vertice no ciclo parcial
    menor = inf # guarda o menor custo encontrado a partir da insercao dos vertices nao visitados
    if len(visitado) >= 2:
        while n < len(visitado)-1:
            i = visitado[n]
            j = visitado[n + 1]
            for k in range(len(grafo)): # k representa o vertice a ser inserido
                if i != j and i != k and k != j and k not in visitado : # quando i, j e k sao iguais a distancia e igual a zero
                    custo = grafo[i][k] + grafo[k][j] - grafo[i][j]
                    if custo < menor:
                        menor = custo
                        indice = ciclo.index(j) 
                        vertice_a_ser_inserido = k
            n += 1
        #print("custo: {}, vertice a ser inserido: {} ".format(custo, vertice_a_ser_inserido))
                
    else:
        if visitado:
            tmp = grafo[visitado[0]]
            tmp[visitado[0]] = inf
            vertice_a_ser_inserido = tmp.index(min(tmp))
            indice = 0
    return indice, vertice_a_ser_inserido



insercao_tsp()