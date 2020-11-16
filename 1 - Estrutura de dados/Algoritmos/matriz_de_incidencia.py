# Grafo nao direcionado nao valorado
import random

class Grafo():
    def __init__(self):
        '''
        Formato da matriz:
        Colunas: arestas
        Linhas: vértices
           a1, a2, a3, a4, a5, a6
        v1[1,  1,  0,  0,  0,  0]
        v2[1,  0,  1,  1,  0,  0]
        v3[0,  1,  1,  0,  1,  0]
        v4[0,  0,  0,  1,  0,  1]
        v5[0,  0,  0,  0,  1,  1]
        Grafo nao orientado 
        '''
        # numero de vertices ja definida, no construtor padrao
        self.numero_vertices = 5
        # vertices presentes no grafo
        self.vertices = [1, 2, 3, 4, 5]
        # as arestas sao representadas pelas colunas na matriz
        self.numero_arestas = 6

        self.matriz_inc = [[1, 1, 0, 0, 0, 0],
                           [1, 0, 1, 1, 0, 0],
                           [0, 1, 1, 0, 1, 0],
                           [0, 0, 0, 1, 0, 1],
                           [0, 0, 0, 0, 1, 1]]    

    def eh_vizinho(self, u, v):
        '''
        Metodo para verificar se dois vertices (u, v) sao adjacentes
        Paremetros:
            u
                vertice presente no grafo
            v
                vertice presente no grafo
        Retorno:
            True ou False
        '''

        vizinho = True
        # A lista self.vertices possui todos os vertices presentes no grafo
        # para saber qual linha da matriz representa cada vertice  que possuem 
        # o mesmo indice
        if u in self.vertices and v in self.vertices:
            u = self.vertices.index(u)
            v = self.vertices.index(v)
            ### Testar ida e volta
            for i in range(self.numero_vertices):
                # As linhas da matriz representam os vertices, para saber se dois vertices sao
                # adjacentes, e preciso checar se (u, v) estao na mesma coluna, ou seja, incidentes
                # a aresta
                if self.matriz_inc[u][i] > 0:
                    if self.matriz_inc[v][i] > 0:
                        vizinho = True
                        return vizinho
                    else:
                        vizinho = False

            return vizinho
        else:
            print("Algum ou ambos os vertices nao estao presentes no grafo")
            
    def retorna_vizinhos(self, u):
        '''
        Retorna os vizinhos de um vertice u
        Parametros:
            u
                vertice presente no grafo para encontrar seus vizinhos
        Retorno:
            vizinho de u
        '''
        u = self.vertices.index(u)
        vizinhos = []
        for i in range(self.numero_arestas):
            if self.matriz_inc[u][i] > 0:
                for j in range(self.numero_vertices):
                    if self.matriz_inc[j][i] > 0:
                        if j != u:
                            vizinhos.append(self.vertices[j])
        return vizinhos
 
    
    def inserir_vertice(self, u):
        '''
        Insere um vertice u na matriz de incidencia, para tanto e preciso 
        adicionar uma nova "linha" na matriz
        '''
        # Caso o vertice u nao exista no grafo, ele sera adicionado
        if u not in self.vertices:
            # lista com o novo vertice que sera adicionado
            novo_vertice = []
            for i in range(self.numero_arestas):
                novo_vertice.append(0)
            # Atualizacao dos numeros e lista de vertices
            self.numero_vertices += 1
            self.vertices.append(u)
            self.matriz_inc.append(novo_vertice)
            print("Matriz apos adicionar o vertice u", u, self.matriz_inc, "\n")
        else:
            print("Vertice ja existe")

    def inserir_aresta(self, u, v, peso):
        '''
        Para inserir uma aresta no grafo, e adicionado a matriz de incidencia 
        uma nova coluna
        '''
        if u in self.vertices and v in self.vertices:
            u = self.vertices.index(u) 
            v = self.vertices.index(v)
            if self.eh_vizinho(u, v):
                print("aresta já existe")
            else:
                for i in range(self.numero_vertices):
                    # teste para verificar a incidencia de u e v a (u, v)
                    # i representa os vertices da matriz
                    if i == u or i == v:
                        self.matriz_inc[i].append(peso)
                    else:
                        self.matriz_inc[i].append(0)
                self.numero_arestas += 1
            print("Matriz de Incidencia ao adicionar aresta: ", self.matriz_inc, "\n")
        else:
            print("Algum dos vertices ou ambos nao estao no grafo")

    def gerar_grafo_arestas(self):
        '''
        Gera um lista com as arestas do grafo a partir da matriz de incidencia
        '''
        aux = []
        arestas = []
        # Na matiriz de incidencia que utilizamos, os vertices adjacentes
        # sao aqueles que possuem valor maior que 0 e que ocupam a mesma coluna
        # da matriz, logo para encontrar os vertices adjacentes, percorremos a matriz
        # e encontramos os indices que representam os vertices adjacentes.
        for i in range(len(self.matriz_inc[0])):
            for j in range(len(self.matriz_inc)):
                if self.matriz_inc[j][i] > 0:
                    aux.append(j)
        
        # As aerstas sao representadas por tuplas (u, v), essa funcao FOR apenas
        # preenche a lista aresta com as arestas.
        for i in range(0, len(aux), 2):
            arestas.append((self.vertices[aux[i]], self.vertices[aux[i+1]]))
     
        return arestas
                   
    
    def remover_vertice(self, u):
        '''
        Para remover um vertice e necessario remover todas as arestas incidentes
        '''        
        colunas = []
        nome = u
        # Para um vertice ser removido, ele precisa existir no grafo
        if u in self.vertices:
            u = self.vertices.index(u)
            # A lista colunas recebe o indice das arestas incidentes ao vertice a ser removido
            for i in range(self.numero_arestas):
                if self.matriz_inc[u][i] > 0:
                    colunas.append(i)
                    #print("colunas i: ", colunas)
        else:
            print("Nao existe o vertice informado no grafo")

        # Primeiro removemos as arestas da matriz, de forma decrescente para nao precisar atualizar
        # o valor dos indices das colunas na matriz
        if colunas:
            for j in range(len(colunas)-1, -1, -1):
                for i in range(self.numero_vertices):                
                    del self.matriz_inc[i][colunas[j]]
        
            # Removemos o vertice, deletando a linha que o representa na matriz
            del self.matriz_inc[u]
            self.numero_vertices -= 1
            self.numero_arestas -= len(colunas)
            self.vertices.remove(nome)       

            print("Matriz ao remover o vertice u:", self.matriz_inc, "\n")
    
    def remover_aresta(self, u, v):
        '''
        Metodo para remover uma aresta por vez do grafo
        Parametros:
            u
                vertice presente no grafo que possui adjacencia a v
            v 
                vertice presente no graof que possui adjacencia a u
        '''
        # Verifica que u e v estao presentes no grafo
        if u in self.vertices and v in self.vertices:
            # Verifica se sao adjacentes
            if self.eh_vizinho(u, v):
                # Atribuicao dos indices dos vertices na matriz
                u = self.vertices.index(u)
                v = self.vertices.index(v)
                for i in range(self.numero_arestas):
                    # Verifica em que posicao se encontra a aresta que queremos remover
                    if self.matriz_inc[u][i] > 0 and self.matriz_inc[v][i] > 0:
                        aresta = i
                for i in range(self.numero_vertices):
                    # A aresta é removida
                    del self.matriz_inc[i][aresta]
                # Atualizacao do numero de arestas
                self.numero_arestas -= 1                
            else:
                print("nao ha aresta")
        else:
            print("Algum dos vertices ou ambos nao existem no grafo")
        
        print("Matriz ao remover a arestas (u, v):", self.matriz_inc, "\n")

    def deletar_grafo(self):
        '''
        Deleta a matriz de incidencia
        '''
        del self.matriz_inc
    
    def matrizInc_para_lista(self):
        '''
        Metodo para passar a matriz de incidencia para lista de adjacencia
        '''
        # Cria a lista
        self.lista_adj = {}
        aux = []
        # Insere todos os vertices como chave do dicionario
        for i in range(self.numero_vertices):
            self.lista_adj.update({self.vertices[i]: {}})    

       
        for i in range(self.numero_vertices):
            # Aux contem os vizinhos de cada vertice presente no grafo
            aux = self.retorna_vizinhos(self.vertices[i])
            for j in range(len(aux)):
                # Insere na lista os vertices adjacentes, como o grafo nao e valorado
                # o peso sempre sera 0
                self.lista_adj[self.vertices[i]].update({aux[j]: 0})
        print("Lista de adjacencia: ", self.lista_adj, "\n")

    def matrizInc_para_matrizAdj(self):
        '''
        Metodo para passar a matriz de incidencia para uma matriz de adjacencia
        '''
        # Criacao da matriz de adjacencia a partir do numero de vertices do grafo
        # Matriz inicializada com 0's
        self.matriz_adj = [
            [0 for x in range(self.numero_vertices)] for y in range(self.numero_vertices)]

        aux = []
        for i in range(self.numero_vertices):
            # Aux recebe todos os vizinhos de cada vertice presente no grafo
            aux = self.retorna_vizinhos(self.vertices[i])
            for j in range(len(aux)):
                # De acordo com a adjacencia dos vertices, caso haja adjacencia
                # as posicoes (i, j) recebem o valor 1
                self.matriz_adj[i][self.vertices.index(aux[j])] = 1
        print("Matriz de adjacencia: ", self.matriz_adj, "\n")


    def gerar_subgrafo_ind_vertices(self):
        '''
        Gera um subgrafo induzido por vertices escolhendo de forma aleatoria a quantidade
        e quais vertices a serem retirados.
        '''
        # De forma aleatoria soa escolhidas a quantidade de vertices a serem removidos
        # e quais vertices serao removidos
        num_of_vertices = len(self.vertices)
        print("Numero de vertices: ", num_of_vertices)
        qntde_vertices_a_remover = random.randrange(0, num_of_vertices+1)
        print("Quantidade de vertices a remover: ", qntde_vertices_a_remover)

        vertices_a_remover = []
        # Os vetices sao escolhidas sem repeticoes a partir de uma lista
        # contendo todos as vertices do grafo
        vertices_a_remover.extend(random.sample(
            self.vertices, qntde_vertices_a_remover))
        print("Vertices a remover: ", vertices_a_remover)

        # Os vertices sao removidos um a um.
        for i in vertices_a_remover:
            self.remover_vertice(i)
        print("Vertices presentes: ", self.vertices)
        print('Matriz atualizada: ', self.matriz_inc, "\n")

    def gerar_subgrafo_ind_arestas(self):
        '''
        Gera um subgrafo induzido por vertices escolhendo de forma aleatoria a quantidade
        e quais vertices a serem retirados.
        '''

        # De forma aleatoria soa escolhidas a quantidade de arestas a serem removidas
        # e quais arestas serao removidas
        print("Numero de arestas: ", len(self.gerar_grafo_arestas()))
        qntde_arestas_a_remover=random.randrange(
            0, len(self.gerar_grafo_arestas())+1)
        print("Quantidade de arestas a remover: ",
              qntde_arestas_a_remover)

        arestas_a_remover = []
        # As arestas sao escolhidas sem repeticoes a partir de uma lista
        # contendo todas as arestas do grafo
        arestas_a_remover.extend(random.sample(
            self.gerar_grafo_arestas(), qntde_arestas_a_remover))
        print("arestas a remover: ", arestas_a_remover)

        for i in range(len(arestas_a_remover)):
            for j in range(1):
                # As arestas sao representadas por tuplas (u, v), 
                # arestas_a_remover[i][j] representa u 
                # e  arestas_a_remover[i][j+1] representa v
                # na lista de arestas que possui seguinte formato:
                # [(u, v), (u, v), ...]
                self.remover_aresta(
                    arestas_a_remover[i][j], arestas_a_remover[i][j+1])

        print('Matriz atualizada: ', self.matriz_inc, "\n")
        

mat_inc = Grafo()
print(mat_inc.eh_vizinho(6, 9))
print("Vizinhos do 2:", mat_inc.retorna_vizinhos(2))
mat_inc.inserir_vertice(7)
mat_inc.inserir_aresta(2, 7, 1)
mat_inc.remover_vertice(4)
mat_inc.remover_aresta(2, 3)
mat_inc.matrizInc_para_lista()
mat_inc.matrizInc_para_matrizAdj()
#mat_inc.gerar_subgrafo_ind_vertices()
#mat_inc.gerar_subgrafo_ind_arestas()

