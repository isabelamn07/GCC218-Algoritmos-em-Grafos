# Algoritmo de Warshall

class Warshall():
    def __init__(self):
        # inicialização de um grafo qualquer
        self.matriz_adj = [[0, 0, 1, 0],
                           [1, 0, 0, 1],
                           [0, 0, 0, 0],
                           [0, 1, 0, 0]]

    def met_warshall(self):
        '''
        Metodo que encontra o fecho transitivo do grafo
        '''
        # checa vertices alcançáveis
        for k in range(len(self.matriz_adj[0])):
            for i in range(len(self.matriz_adj[0])):
                for j in range(len(self.matriz_adj[0])):
                        self.matriz_adj[i][j] = self.matriz_adj[i][j] or (
                          self.matriz_adj[i][k] and self.matriz_adj[k][j])

        return self.matriz_adj


grafo = Warshall()
print(grafo.met_warshall())

