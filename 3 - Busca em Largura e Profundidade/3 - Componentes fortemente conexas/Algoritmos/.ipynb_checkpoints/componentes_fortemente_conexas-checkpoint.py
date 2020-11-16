'''
COMPONENTES-FORTEMENTE-CONEXAS(G)
1 chamar a rotina DFS(G) para encontrar os tempos de finalização u.f para cada vertice u. 
    Retorne um vetor com os tempos de finalização u.f.
2 ache o grafo transposto GT
3 para cada vertice do vetor encontrado na linha (1) que ainda não tenha sido visitado, 
    chamamos DFS(GT) e encontramos cada componente fortemente conexa.
4 como saída, teremos cada floresta da árvore.
'''
'''
matriz_adjacencia = [[0, 0, 1, 1, 0],
                     [1, 0, 0, 0, 0],
                     [0, 1, 0, 0, 1],
                     [0, 0, 0, 0, 1],
                     [0, 0, 1, 0, 0]]
                                          
'''
matriz_adjacencia = [[0, 1, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 0, 1, 1, 0, 0],
                     [0, 0, 0, 1, 0, 0, 1, 0],
                     [0, 0, 1, 0, 0, 0, 0, 1],
                     [1, 0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 0],
                     [0, 0, 0, 0, 0, 1, 0, 1],
                     [0, 0, 0, 0, 0, 0, 0, 1]]

# lista de vertices do grafo
vertices = [i for i in range(len(matriz_adjacencia))]
# lista de vertices ja visitados
vertice_visitado = []
# lista com a ordem de tempo final dos vertices
ordenacao = []
# lista com vertices ja visitados
visitado = []
# lista com cada ciclo que forma uma componente conexa
ciclo = []
# lista que contém o status de cada vértice (Branco, Cinza, Preto), assim como o vértice pai e o tempo
grafo_dfs = []
# lista com todos a componentes fortemente conexas
componentes_fconexas = []

###--------------------------------------------------------------------------------------------------###
# PRIMEIRA PARTE DO ALGORITMO - BUSCA EM PROFUNDIDADE PARA DEFINIR A ORDENACAO POR ORDEM DE TEMPO FINAL
# OU FECHAMENTO DO VERTICE (QUANDO O VERTICE TORNA-SE PRETO E NAO E MAIS VISITADO)


def grafo_inicial_dfs():
    grafo_inicial = []
    for i in range(len(vertices)):
        grafo_inicial.append([i, 'BRANCO', None])
    return grafo_inicial


def dfs(Grafo):
    '''
    Função para inicializar os valores como: cor, pai, tempo
    Parâmetros:
        Grafo
            grafo a ser percorrido pela busca em profundidade
    '''
    # Inicialização de valores    
    grafo_dfs.extend(grafo_inicial_dfs())

    for i in range(len(vertices)):
        # caso o vertice nao tenha sido visitado, e realizada a busca em profundidade(teste para todos os vertices)
        if grafo_dfs[i][0] not in vertice_visitado:
            dfs_visit(Grafo, grafo_dfs[i][0])

def dfs_visit(Grafo, u):
    # encontrando o indice do vertice u no grafo_dfs
    for i in range(len(grafo_dfs)):
        if grafo_dfs[i][0] == u:
            indice = i
    # O vértice sendo explorado, recebe a cor cinza
    grafo_dfs[indice][1] = 'CINZA'
    vertice_visitado.append(grafo_dfs[indice][0])

    ind = 0
    for i in range(len(Grafo)):
        if Grafo[u][i] == 1 and (vertices[i] not in vertice_visitado):
            v = vertices[i]
            ind = i
        
        if grafo_dfs[ind][1] == 'BRANCO':
            grafo_dfs[ind][2] = u
            dfs_visit(Grafo, v)

    for i in range(len(grafo_dfs)):
        if grafo_dfs[i][0] == u:
            grafo_dfs[i][1] = 'PRETO'

            ordenacao.append(u)

###--------------------------------------------------------------------------------------------------###
# FUNCAO PARA TRANSPOR O GRAFO
def grafo_transposto(Grafo):
    grafo_trans = []
    for i in range(len(Grafo)):
        linha_coluna = []
        for j in range(len(Grafo)):
            linha_coluna.append(Grafo[j][i])
        grafo_trans.append(linha_coluna)

    return grafo_trans

###--------------------------------------------------------------------------------------------------###
### SEGUNDA PARTE 
### ENCONTRAMOS CADA COMPONENTE FORTEMENTE CONEXA DO GRAFO
def dfs_visit2(Grafo, u, grafo_final_dfs):
    
    for i in range(len(grafo_final_dfs)):
        if grafo_final_dfs[i][0] == u:
            indice = i

    grafo_final_dfs[indice][1] = 'CINZA'
    visitado.append(grafo_final_dfs[indice][0])

    ind = 0
    for i in range(len(Grafo)):
        if Grafo[u][i] == 1 and vertices[i] not in visitado:
            v = vertices[i]
            ind = i

            if grafo_final_dfs[ind][1] == 'BRANCO':
                grafo_final_dfs[ind][2] = u
                dfs_visit2(Grafo, v, grafo_final_dfs)
    for i in range(len(grafo_final_dfs)):
        if grafo_final_dfs[i][0] == u:
            grafo_final_dfs[i][1] = 'PRETO'
            ciclo.append(u)


aux = []
def dfs_connected(pilha):
    while pilha:
        vertice_inicial = pilha.pop()
        dfs_visit2(grafo_t, vertice_inicial, grafo_inicial_dfs())

        if (len(ciclo) > 1):
            aux = ciclo[:]
            componentes_fconexas.append(aux)

        elif (len(ciclo) == 1 and matriz_adjacencia[ciclo[0]][ciclo[0]] > 0):
            aux = ciclo[:]
            componentes_fconexas.append(aux)
  
        ciclo.clear()

dfs(matriz_adjacencia)
grafo_t = grafo_transposto(matriz_adjacencia)
dfs_connected(ordenacao)
print(componentes_fconexas)
