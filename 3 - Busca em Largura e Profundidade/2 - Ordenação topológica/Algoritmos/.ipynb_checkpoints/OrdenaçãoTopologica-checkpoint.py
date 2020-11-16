import random

## Para encontrar a ordenação topológica utilizamos a busca em profundidade e calculamos o tempo de fechamento de cada
## vertice
## A ordenação é realizada na ordem de fechamento dos vertices, então adicionamos cada vertice "fechado" a uma lista
## Essa lista contém a ordem topológica.

# variável com o controle de tempo de descoberta e fechamento do vértice
tempo = 0
# lista que contém o status de cada vértice (Branco, Cinza, Preto), assim como o vértice pai e o tempo
grafo_dfs = []
# lista que contém os vértices que já foram visitados
visitado = []
# lista que vai receber os vertices ordenados topologicamente
top = []

def DFS(Grafo):
    '''
    Função para inicializar os valores como: cor, pai, tempo
    Parâmetros:
        Grafo
            grafo a ser percorrido pela busca em profundidade
    '''
    
    # randomização dos vértices do grafo para realizar a busca em profundidade iniciando de qualquer vértice no grafo
    vertices_randomizados = list(Grafo.keys())
    random.shuffle(vertices_randomizados) 
    
    # Inicialização de valores
    for i in vertices_randomizados:
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
            grafo_dfs[i][1] = 'PRETO'
            tempo += 1
            grafo_dfs[i].append(('tempo de fechamento:' , tempo))
            top.insert(0, u)
            
lista_adj = {
    'PG': {'VT': 0},
    'CA': {'VT': 0},
    'CB': {'BA': 0},
    'BA': {'PC': 0},
    'PC': {'VT':0 },
    'VT': {},    
}

DFS(lista_adj)

print("Ordem topologica ", (top))
print('DFS:')
print(grafo_dfs)

## *Existem varias possiveis configuracoes da ordenacao topologica das atividades