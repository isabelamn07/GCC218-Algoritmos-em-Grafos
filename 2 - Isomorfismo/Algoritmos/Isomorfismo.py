# Grafos isomorfos

#Grafo1
## Se ao rearrumar os vertices, conseguirmos obter a mesma matriz de adjacência, os grafos são isomorfos.
# Se conseguirmos achar a bijecao conseguimos definir se os grafos são isomorfos ou não.

grafo_G = [[0, 0, 0, 1, 1],
          [0, 0, 1, 0, 1],
          [0, 1, 0, 1, 0],
          [1, 0, 1, 0, 0],
          [1, 1, 0, 0, 0]]
grafo_G1 = [[0, 1, 1, 0, 0],
            [1, 0, 0, 1, 0],
            [1, 0, 0, 0, 1],
            [0, 1, 0, 0, 1],
            [0, 0, 1, 1, 0]]

bijecoes = [(0, 0), (1, 4), (2, 3), (3, 1), (4, 2)]

def bijecao():
    '''
    Teste se as matrizes são iguais dadas as bijeções
    '''
    for i in range(len(grafo_G)):
        for j in range(len(grafo_G[i])):
            if grafo_G[i][j] > 0:
                if (grafo_G1[bijecoes[i][1]][bijecoes[j][1]] > 0):
                    isomorfo = True         
                else: 
                    return False       
    return isomorfo
               
    
if bijecao():
    print("Grafo isomorfo")




