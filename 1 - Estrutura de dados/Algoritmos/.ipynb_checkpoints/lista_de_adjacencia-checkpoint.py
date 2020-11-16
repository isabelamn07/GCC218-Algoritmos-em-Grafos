import random

class Grafo:
    def __init__(self, direcionado=False, valorado=False, grafo_lista_adjacencia=[]):
        '''
        Construtor padrao
        Parametros:
            direcionado
                indicado se o grafo e direcionado ou nao
            valorado
                indica se o grafo e valorado ou nao
        '''
        self.grafo_direcionado = direcionado
        self.grafo_valorado = valorado
        self.lista_de_adjacencia = grafo_lista_adjacencia
        self.copia_grafo_original = self.lista_de_adjacencia.copy()
    
    def eh_vizinho(self, u, v):
        '''
        Verifica se existe adjacencia entre dois vertices
        Parametros:
            u
                um vertice presente no grafo
            v 
                um vertice presente no grafo
        Retorno:
            Verdadeiro ou Falso
        '''
        # Para verificar a relacao de adjacencia entre dois vertices, os mesmos
        # precisam estar presentes no grafo
        if u in self.lista_de_adjacencia:
            if v in self.lista_de_adjacencia[u]:
                return True
        else:
            print('Vertice u informado nao existe no grafo')
            return False
        return False

    def retorna_vizinhos(self, u):
        '''
        Retorna todos os vertices adjacentes de um vertice passado por parametro
        Parametros
            u
                um vertice presente no grafo
        Retorno 
            vetices adjacente a u e seus respectivos pesos

        '''
        if u in self.lista_de_adjacencia:
            return self.lista_de_adjacencia[u]
        else:
            print("Vertice nao encontrado! \n")

    def inserir_vertice(self, u, v, peso):
        '''
        Insere um vertice no grafo e cria uma aresta ligada a um vertice v ja existente no grafo
        Parametros:
            u
                vertice a ser inserido
            v
                vertitice adjacente
            peso
                peso da aresta que liga (u, v)
        '''
        if u not in self.lista_de_adjacencia and v in self.lista_de_adjacencia:
            self.lista_de_adjacencia.update({u: {v: peso}})
            # Como o grafo e nao direcionado, temos que adicionar a adjacencia do vertice u
            # recem criado ao vetice v
            if not self.grafo_direcionado:
                self.lista_de_adjacencia[v].update({u: peso})

        print("Lista ao adicionar um vértice u e uma aresta ligada a um vértice v: ",
              self.lista_de_adjacencia, "\n")

    def inserir_vertice_isolado(self, u):
        '''
        Insere um vertice, caso ele ainda nao exista no grafo, porem sem adicionar nenhum vertice adjacente e peso
        Parametros:
            u
                vertice a ser inserido
        '''
        if u not in self.lista_de_adjacencia:
            # cria a chave com o vertice criado sem nenhum vertice adjacente e peso
            self.lista_de_adjacencia.update({u: {}})
            print("Estrutura ao adicionar um vertice isolado: ", self.lista_de_adjacencia, "\n")
        else:
            print("Vertice ja existe na lista")

    def inserir_aresta(self, u, v, peso):
        '''
        Insere aresta, caso existam no grafo os vertice u e v
        Parametros:
            u
                vertice presente no grafo
            v 
                vertice presente no grafo
            peso
                valor da aresta
        '''
        if u and v in self.lista_de_adjacencia and v not in self.lista_de_adjacencia[u]:
            # Como o grafo e nao direcionado e preciso adicionar a adjacencia dos vertices nas
            # duas chaves dentro da lista
            self.lista_de_adjacencia[u].update({v: peso})
            self.lista_de_adjacencia[v].update({u: peso})
            print("Grafo ao adicionar uma aresta: ", self.lista_de_adjacencia, "\n")

    def gerar_lista_de_arestas(self):
        '''
        Gera uma lista com o conjunto de pares ordenados com todas as arestas do grafo
        '''
        arestas = []
        for i in self.lista_de_adjacencia.keys():
            for j in self.lista_de_adjacencia[i]:
                if (i, j) not in arestas and (j, i) not in arestas:
                    arestas.append((i, j))

        return arestas

    def remover_vertice(self, u):
        '''
        Ao remover um vertice do grafo, e necessario tambem remover as arestas ligadas a ele
        '''
        # Para ser removido o vertice u precisa existir na lista de adjacencia
        if u in self.lista_de_adjacencia:
            self.lista_de_adjacencia.pop(u)
            # O vertice deve ser removido nao apenas nas chaves da lista de adjacencia
            # dentro do dicionario, mas tambem nos itens que tem relacao a chave u, por exemplo:
            # 1: { 2: 20, 3: 7},
            # 2: { 1: 20}
            # remover_vertice(1)
            # 1: { 3: 6},
            # 2: {}
            for i, j in self.lista_de_adjacencia.items():
                if u in j:
                    j.pop(u)
            print("Lista apos a remocao do vertice u: ",
                  u, self.lista_de_adjacencia, "\n")
        else:
            print("Vertice nao encontrado \n")

    def remover_aresta(self, u, v):
        '''
        Para remover uma aresta, e necessario que os vertices ligados por ela estejam presentes
        no grafo
        '''
        if u in self.lista_de_adjacencia:
            if v in self.lista_de_adjacencia[u]:
                # remove a representacao de adjacencia da chave u
                self.lista_de_adjacencia[u].pop(v)
                # remove a representacao de adjacencia da chave v
                if u in self.lista_de_adjacencia[v]:
                    self.lista_de_adjacencia[v].pop(u)
                print("Lista apos remocao de uma aresta: ", self.lista_de_adjacencia, "\n")
            else:
                print('Vertice v nao encontrado')
        else:
            print('Vertice u nao encontrado')
        

    def deletar_grafo(self):
        '''
        Deleta o grafo
        '''
        self.lista_de_adjacencia.clear()
        # del self.lista_de_adjacencia
        #print(self.lista_de_adjacencia)

    def get_lista(self):
        '''
        retonar o grafo 
        '''
        return self.lista_de_adjacencia

    def lista_para_matriz_de_adjacencia(self):
        '''
        Transforma a lista de adjacencia atual em uma matriz de adjacencia
        '''

        #cria uma matriz n x n de acordo com a quantidade de vertices do grafo
        self.matriz_de_adjacencia = [
            [0 for x in range(len(self.lista_de_adjacencia))] for y in range(len(self.lista_de_adjacencia))]

        #lista que contem os vertices presentes no grafo na ordem que aparecem na lista de ajcencia,
        #importante para saber o indice dos vertices na matriz
        posicoes = []
        for i in self.lista_de_adjacencia.keys():
            posicoes.append(i)
        print("Vertices: ", posicoes)

        for i in self.lista_de_adjacencia.keys():
            for j in self.lista_de_adjacencia[i].keys():
                if self.lista_de_adjacencia[i][j] != 0:
                    self.matriz_de_adjacencia[posicoes.index(i)][posicoes.index(
                        j)] = self.lista_de_adjacencia[i][j]
                else:
                    self.matriz_de_adjacencia[posicoes.index(i)][posicoes.index(
                        j)] = 1

        print("Matriz de adjacencia: ", self.matriz_de_adjacencia, "\n")

    def lista_para_matriz_de_incidencia(self):
        '''
        Transforma a lista de adjacencia atual em uma matriz de incidencia
        '''
        # A lista arestas possui todos os pares ordenados de vertices adjacentes, ou seja, as arestas.
        # As arestas representam as colunas em nossa matriz de incidencia
        arestas = []
        arestas.extend(self.gerar_lista_de_arestas())
        print("Arestas: ", arestas)

        #Cria uma matriz de zeros numero de vertices x numero de arestas
        self.matriz_de_incidencia = [
            [0 for x in range(len(arestas))] for y in range(len(self.lista_de_adjacencia))]

        #lista com todos os vertices do grafo, na ordem que aparecem na lista de adjacencia
        vertices = []
        for i in self.lista_de_adjacencia.keys():
            vertices.append(i)

        # Verifica a existencia de cada vertice em cada relacao (u, v), caso exista
        # e atribuido a cada posicao da matriz o valor 1 que representa a existencia
        # da incidencia

                
        if not self.grafo_valorado and not self.grafo_direcionado:
            for i in range(len(vertices)):
                for j in range(len(arestas)):
                    # verifica adjacencia para indicar a incidencia
                    if vertices[i] in arestas[j]:
                        self.matriz_de_incidencia[i][j] = 1
                        self.matriz_de_incidencia[vertices.index(arestas[j][1])][j] = 1
                        
        if not self.grafo_valorado and self.grafo_direcionado:
            for i in range(len(vertices)):
                for j in range(len(arestas)):
                    # verifica adjacencia para indicar a incidencia
                    if vertices[i] in arestas[j]:
                        if arestas[j][0] != arestas[j][1]:
                            self.matriz_de_incidencia[i][j] = 1
                            self.matriz_de_incidencia[vertices.index(arestas[j][1])][j] = -1
                        else:
                            self.matriz_de_incidencia[i][j] = 2

                        
        elif self.grafo_direcionado and self.grafo_valorado:
            for i in range(len(vertices)):
                for j in range(len(arestas)):
                    # verifica adjacencia para indicar incidencia
                    if vertices[i] in arestas[j] and vertices[i] == arestas[j][0]:
                        self.matriz_de_incidencia[i][j] =  self.matriz_de_adjacencia[vertices.index(arestas[j][0])][vertices.index(arestas[j][1])]
                    elif vertices[i] in arestas[j] and vertices[i] == arestas[j][1]:
                        self.matriz_de_incidencia[i][j] =  -self.matriz_de_adjacencia[vertices.index(arestas[j][0])][vertices.index(arestas[j][1])]
        
        elif self.grafo_direcionado and not self.grafo_valorado:
            for i in range(len(vertices)):
                for j in range(len(arestas)):
                    # verifica adjacencia para indicar incidencia
                    if vertices[i] in arestas[j] and vertices[i] == arestas[j][0]:
                        self.matriz_de_incidencia[i][j] =  1
                    elif vertices[i] in arestas[j] and vertices[i] == arestas[j][1]:
                        self.matriz_de_incidencia[i][j] =  -1
      


        print("Matriz Incidencia: ", self.matriz_de_incidencia, "\n")

    def gerar_subgrafo_ind_vertices(self):
        '''
        Gera um subgrafo induzido por vertices escolhendo de forma aleatoria a quantidade
        e quais vertices a serem retirados.
        '''

        num_of_vertices = len(self.lista_de_adjacencia.keys())
        print("Numero de vertices: ", num_of_vertices)
        qntde_vertices_a_remover = random.randrange(0, num_of_vertices+1)
        print("Quantidade de vertices a remover: ", qntde_vertices_a_remover)

        vertices_a_remover = []
        vertices_a_remover.extend(random.sample(
            self.lista_de_adjacencia.keys(), qntde_vertices_a_remover))
        print("Vertices a remover: ", vertices_a_remover)

        for i in vertices_a_remover:
            self.remover_vertice(i)

        print('Lista atualizada: ', self.lista_de_adjacencia)

    def gerar_subgrafo_ind_arestas(self):
        '''
        Gera um subgrafo induzido por vertices escolhendo de forma aleatoria a quantidade
        e quais vertices a serem retirados.
        '''
        arestas = self.gerar_lista_de_arestas()
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

        print('Lista atualizada: ', self.lista_de_adjacencia)

    def main(self):
        print("2 e 7 sao vizinhos?: ", self.eh_vizinho(2, 7))
        print("Vizinhos do vertice 5: ", self.retorna_vizinhos(5))
        self.inserir_vertice(98, 6, 12)
        self.inserir_vertice(13, 5, 8)
        self.inserir_vertice(9, 2, 35)
        self.inserir_vertice_isolado(22)
        self.inserir_aresta(1, 7, 68)
        self.remover_vertice(6)
        self.remover_aresta(1, 6)
        #self.deletar_grafo()
        self.lista_para_matriz_de_adjacencia()
        self.lista_para_matriz_de_incidencia()
        self.gerar_subgrafo_ind_vertices()
        self.gerar_subgrafo_ind_arestas()
        

import networkx as nx
import matplotlib.pyplot as plt


if __name__ == '__main__':
    #Dicionario no formato:
    #vertice: {vertice_adjacente: peso_da_aresta}
    lista_adjacencia = {1: {2: 18, 3: 33}, 2: {}, 3: {}, 4: {1: 22, 2: 25, 5: 49}, 5: {2: 7}}
    grafo = Grafo(True, True, lista_adjacencia)    
    
    
    # Desenhando o grafo com networkx e matplotlib
    G = nx.DiGraph(grafo.copia_grafo_original)
    pos = nx.spring_layout(G)
    
    # Vertices
    nx.draw_networkx_nodes(G, pos, node_size=900)
   
    #Arestas
    labels_arestas = {}
    arestas = []
    for i in grafo.copia_grafo_original:
        for j in grafo.copia_grafo_original[i]:
            if (j, i) not in labels_arestas:
                labels_arestas.update({(i,j) : str(grafo.copia_grafo_original[i][j])})
                arestas.append((i, j))
    nx.draw_networkx_edges(G, pos, edgelist=arestas, width=2)
    
    # Labels
    nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif', font_color='w')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels_arestas, font_color='r', label_pos=0.5, font_weight=600)
    plt.axis('off')
    plt.show()
    
    grafo.main()