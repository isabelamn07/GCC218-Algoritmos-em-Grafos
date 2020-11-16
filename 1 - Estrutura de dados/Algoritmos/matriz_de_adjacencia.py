
## Matriz de adjacencia

import random

class Grafo():
    def __init__(self):
        # Tamanho da matriz
        self.tamanho_matriz = 5
        # Criacao da matriz de adjacencia com zeros em todas as posicoes
        self.matrizAdj = [[0 for x in range(self.tamanho_matriz)] for y in range(self.tamanho_matriz)]
        # A lista vertices contem todos os vertices presentes no grafo, a lista e atualizada a cada remocao
        # ou insercao, como nao existe ordem para adicionar vertices essa lista e importante para encontrar
        # os indices na matriz
        self.vertices = []
        for i in range(1, self.tamanho_matriz+1, 1):
            self.vertices.append(i)

    def criar_grafo(self):
       '''
       Funcao para atribuir de forma aleatoria o valor 1 para indicar adjacencia entre vertices
       ''' 
       for i in range(self.tamanho_matriz):
            for j in range(self.tamanho_matriz):
                aleatorio = random.uniform(0, 1)
                if aleatorio > 0.5:
                    self.matrizAdj[i][j] = 1
                    self.matrizAdj[j][i] = 1

        #print(self.matrizAdj)

    def eh_vizinho(self, u, v):
        '''
        Funcao que recebe dois vertices e verifica se ambos sao adjacentes 
        um vertice e considerado adjacente ao outro em uma matriz de adjacencia se
        nas posicoes [u][v] e [v][u] para grafos nao direcionados e [u][v] para grafos
        direcionados o valor na matriz for maior que 0
        '''
        # u  e v recebem o valor de seu indice na matriz
        u = self.vertices.index(u)
        v = self.vertices.index(v)
        if self.matrizAdj[u][v] > 0:
            return True
        else:
            return False

    def retorna_vizinhos(self, u):
        '''
        Retorna todos os vertices adjacentes ao vertice u passado por parametro
        '''
        
        vizinhos = []
        # u precisa estar presente no grafo
        if u in self.vertices:
            u = self.vertices.index(u)
            for i in range(len(self.matrizAdj)):
                # Os vizinhos de u, sao os valores de v que tem valor maior que 0 na linha 
                # do vertice u da matriz
                if self.matrizAdj[u][i] == 1:
                    index = self.vertices[i]
                    vizinhos.append(index)
            return vizinhos

    
    def inserir_vertice(self, u, v, peso):
        '''
        Insere um vertice por vez na matriz
        '''
        if v in self.vertices:
            v = self.vertices.index(v)
        if u not in self.vertices:
            self.vertices.append(u)
            u = self.vertices.index(u)
            self.tamanho_matriz += 1
            for i in range(len(self.matrizAdj)):
                self.matrizAdj[i].append(0)
            linha = []
            for j in range(self.tamanho_matriz):
                linha.append(0)
            self.matrizAdj.append(linha)
            self.matrizAdj[u][v] = 1
               
            print("Matriz de adjacencia apos inserir o vertice : ", u, self.matrizAdj, "\n")

    
    def inserir_aresta(self, u, v):
        '''
        Insere uma aresta no grafo, que e basicamente atribuir um valor maior
        que zero na matriz de adjacencias para u, v
        '''
        if u in self.vertices and v in self.vertices:
            u = self.vertices.index(u)
            v = self.vertices.index(v)
            self.matrizAdj[u][v] = 1
            self.matrizAdj[v][u] = 1
        else:
            print("Algum dos vertices ou ambos nao existem")
    
    def gerar_lista_de_arestas(self):
        '''
        Retorna um lista contendo todas arestas do grafo (u, v)
        '''
        arestas = []
        for i in self.vertices:
            for j in self.vertices:
                # Se os vertices forem adjacentes na matriz, (u, v) e adicionado a arestas
                if self.matrizAdj[self.vertices.index(i)][self.vertices.index(j)] > 0 and (j, i) not in arestas:
                    arestas.append((i, j))
        return arestas

    def remover_vertice(self, u):
        '''
        Remove um vertice da matriz, para tanto a funcao remove a linha e a coluna
        do vertice passado por parametro
        '''
        if u in self.vertices:
            aux = u
            u = self.vertices.index(u)
            self.vertices.remove(self.vertices[u])
            # deleta toda a linha que corresponde ao vertice u
            del self.matrizAdj[u]
            for i in range(len(self.matrizAdj)):
                # deleta toda a coluna do vertice u
                del self.matrizAdj[i][u]

            print("Matriz ao remover o vertice u: ", aux, self.matrizAdj, "\n")

    def remover_aresta(self, u, v):
        '''
        Remove uma aresta (u, v), para tanto basta na matriz atribuir o valor 0
        que reprensenta que dois vertices nao sao adjacentes
        '''
        if u in self.vertices and v in self.vertices:
            aux1 = u
            aux2 = v
            u = self.vertices.index(u)
            v = self.vertices.index(v)
            # Como o grafo e nao direcionado, removemos as arestas de (u, v) e (v, u),
            # se o grafo fosse direcionado apenas (u, v) seria removida
            self.matrizAdj[u][v] = 0
            self.matrizAdj[v][u] = 0
            print("Matriz de adjacencia ao remover (u,v) ",
                  aux1, aux2, self.matrizAdj, "\n")
        else:
            print("Algum dos vertices ou ambos nao existem no grafo")
       

       

    def deletar_grafo(self):
        '''
        Deleta a matriz
        '''
        del self.matrizAdj

    def matrizAdj_para_lista(self):
        '''
        Metodo para tranforma a matriz de adjacencia em lista de adjacencia, a lista
        de adjacencia usa a estrutura dict
        '''
        # A lista adjacencias recebe as listas com os vizinhos de cada vertice presente
        # no grafo
        adjacencias = []
        for i in self.vertices:
            adjacencias.append(self.retorna_vizinhos(i))

        self.lista_adjacencia = {}
        for i in self.vertices:
            self.lista_adjacencia.update({i: {}} )   
        for j in range(len(adjacencias)):
            for f in range(len(adjacencias[j])):
                self.lista_adjacencia[self.vertices[j]].update({adjacencias[j][f]: 0})
        
        #print('Adjacencias', adjacencias)
        print("Lista de adjacencia: ", self.lista_adjacencia)

    def matrizAdj_para_matrizInc(self):
        '''
        Metodo para criar uma matriz de incidencia a partir de uma matriz de adjacencia
        '''
        print(self.vertices)
        arestas = []
        arestas = (self.gerar_lista_de_arestas())        

        # cria uma matriz com tamanho num_vertices x num_arestas de zeros
        self.matrizInc = [
            [0 for x in range(len(arestas))] for y in range(self.tamanho_matriz)]
        
        for i in range(len(self.vertices)):
            for j in range(len(arestas)):
                # verifica adjacencia para indicar incidencia
                if self.vertices[i] in arestas[j]:
                    self.matrizInc[i][j] = 1
      

        #print("Arestas: ", arestas)
        print("Matriz de incidencia: ", self.matrizInc, "\n")

    def gerar_subgrafo_ind_vertices(self):
        '''
        Gera um subgrafo induzido por vertices escolhendo de forma aleatoria a quantidade
        e quais vertices a serem retirados.
        '''

        num_of_vertices = len(self.vertices)
        print("Numero de vertices: ", num_of_vertices)
        qntde_vertices_a_remover = random.randrange(0, num_of_vertices+1)
        print("Quantidade de vertices a remover: ", qntde_vertices_a_remover)

        vertices_a_remover = []
        vertices_a_remover.extend(random.sample(
            self.vertices, qntde_vertices_a_remover))
        print("Vertices a remover: ", vertices_a_remover)

        for i in vertices_a_remover:
            self.remover_vertice(i)
        print("Vertices presentes: ", self.vertices)
        print('Matriz atualizada: ', self.matrizAdj, "\n")

    def gerar_subgrafo_ind_arestas(self):
        '''
        Gera um subgrafo induzido por vertices escolhendo de forma aleatoria a quantidade
        e quais vertices a serem retirados.
        '''
        arestas = []
        arestas.extend(self.gerar_lista_de_arestas())
        print('Arestas presentes: ', arestas)
        print("Numero de arestas: ", len(arestas))
        qntde_arestas_a_remover = random.randrange(0, len(arestas)+1)
        print("Quantidade de arestas a remover: ",
              qntde_arestas_a_remover)

        arestas_a_remover = []
        arestas_a_remover.extend(random.sample(
            arestas, qntde_arestas_a_remover))
        print("arestas a remover: ", arestas_a_remover)

        for i in range(len(arestas_a_remover)):
            for j in range(1):
                self.remover_aresta(
                    arestas_a_remover[i][j], arestas_a_remover[i][j+1])

        print("Arestas presentes: ", self.gerar_lista_de_arestas())
        print('Matriz atualizada: ', self.matrizAdj, "\n")
        


grafo = Grafo()
grafo.criar_grafo()
print(grafo.eh_vizinho(1, 3))
print(grafo.retorna_vizinhos(5))
grafo.inserir_vertice(6, 2, 0)
grafo.inserir_aresta(1, 6)
grafo.remover_aresta(2, 4)
grafo.remover_vertice(3)
#grafo.deletar_grafo()
grafo.matrizAdj_para_lista()
grafo.matrizAdj_para_matrizInc()
#grafo.gerar_subgrafo_ind_vertices()
#grafo.gerar_subgrafo_ind_arestas()


    
