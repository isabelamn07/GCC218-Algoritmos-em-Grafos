import random
### Grafos ###

# Grafo nao orientado, valorado


class Graph:
    def __init__(self):
        '''Construtor padrao'''
        #Dicionario no formato:
        #vertice: {vertice_adjacente: peso_da_aresta}
        # self.dicionario = {
        #     1: {2: 4, 5: 9, 6: 8},
        #     2: {1: 4, 3: 6, 4: 6, 7: 12},
        #     3: {2: 6, 6: 23, 5: 11, 7: 55},
        #     4: {2: 6, 5: 99, 6: 46, 7: 19},
        #     5: {1: 9, 3: 11, 4: 99},
        #     6: {1: 8, 3: 23, 4: 46},
        #     7: {2: 12, 3: 55, 4: 19}
        # }
        self.dicionario = { 'S': {'B': 1, 'D': 3},
          'A': {'C': 9},
          'B': {'A': 5, 'D':12},
          'C': {'B': 7, 'T': 2},
          'D': {'C': 5, 'E': 6, 'F': 2},
          'E': {'C': 4, 'T': 1},
          'F': {'E': 21, 'T': 8}, 
          'T': {}
}

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
        if u in self.dicionario:
            if v in self.dicionario[u]:
                return True
        else:
            print('Vertice u informado nao existe no grafo')
            return False
        return False

    def retorna_vizinhos(self, u):
        '''
        Retorna todos os vertices adjacentes de um dado vertice
        Parametros:
            u
                um vertice presente no grafo
        Retorno: 
            vetices adjacente a u e seus respectivos pesos

        '''
        if u in self.dicionario:
            return self.dicionario[u]
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
        if u not in self.dicionario and v in self.dicionario:
            self.dicionario.update({u: {v: peso}})
            # Como o grafo e nao direcionado, temos que adicionar a adjacencia do vertice u
            # recem criado ao vetice v
            self.dicionario[v].update({u: peso})

        print("Lista ao adicionar um vértice u e uma aresta ligada a um vértice v: ",
              self.dicionario, "\n")

    def inserir_vertice_isolado(self, u):
        '''
        Insere um vertice, caso ele ainda nao exista no grafo, porem sem adicionar nenhum vertice adjacente e peso
        Parametros:
            u
                vertice a ser inserido
        '''
        if u not in self.dicionario:
            # cria a chave com o vertice criado sem nenhum vertice adjacente e peso
            self.dicionario.update({u: {}})
            print("Estrutura ao adicionar um vertice isolado: ", self.dicionario, "\n")
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
        if u and v in self.dicionario and v not in self.dicionario[u]:
            # Como o grafo e nao direcionado e preciso adicionar a adjacencia dos vertices nas
            # duas chaves dentro da lista
            self.dicionario[u].update({v: peso})
            self.dicionario[v].update({u: peso})
            print("Grafo ao adicionar uma aresta: ", self.dicionario, "\n")

    def gerar_lista_de_arestas(self):
        '''
        Gera uma lista com o conjunto de pares ordenados com todas as arestas do grafo
        '''
        arestas = []
        for i in self.dicionario.keys():
            for j in self.dicionario[i]:
                if not arestas:
                    arestas.append((i, j))
                elif (j, i) not in arestas:
                    arestas.append((i, j))
        return arestas

    def remover_vertice(self, u):
        '''
        Ao remover um vertice do grafo, e necessario tambem remover as arestas ligadas a ele
        '''
        # Para ser removido o vertice u precisa existir na lista de adjacencia
        if u in self.dicionario:
            self.dicionario.pop(u)
            # O vertice deve ser removido nao apenas nas chaves da lista de adjacencia
            # dentro do dicionario, mas tambem nos itens que tem relacao a chave u, por exemplo:
            # 1: { 2: 20, 3: 7},
            # 2: { 1: 20}
            # remover_vertice(1)
            # 1: { 3: 6},
            # 2: {}
            for i, j in self.dicionario.items():
                if u in j:
                    j.pop(u)
            print("Lista apos a remocao do vertice u: ",
                  u, self.dicionario, "\n")
        else:
            print("Vertice nao encontrado \n")

    def remover_aresta(self, u, v):
        '''
        Para remover uma aresta, e necessario que os vertices ligados por ela estejam presentes
        no grafo
        '''
        if u in self.dicionario:
            if v in self.dicionario[u]:
                # remove a representacao de adjacencia da chave u
                self.dicionario[u].pop(v)
                # remove a representacao de adjacencia da chave v
                self.dicionario[v].pop(u)
                print("Lista apos remocao de uma aresta: ", self.dicionario, "\n")
            else:
                print('Vertice v nao encontrado')
        else:
            print('Vertice u nao encontrado')
        

    def deletar_grafo(self):
        '''
        Deleta o grafo
        '''
        self.dicionario.clear()
        #print(self.dicionario)

    def get_lista(self):
        '''
        retonar o grafo 
        '''
        return self.dicionario

    def lista_para_matrizAdj(self):
        '''
        Transforma a lista de adjacencia atual em uma matriz de adjacencia
        '''

        #cria uma matriz n x n de acordo com a quantidade de vertices do grafo
        self.matrizAdj = [
            [0 for x in range(len(self.dicionario))] for y in range(len(self.dicionario))]

        #lista que contem os vertices presentes no grafo na ordem que aparecem na lista de ajcencia,
        #importante para saber o indice dos vertices na matriz
        posicoes = []
        for i in self.dicionario.keys():
            posicoes.append(i)
        print("Vertices: ", posicoes)

        for i in self.dicionario.keys():
            for j in self.dicionario[i].keys():
                self.matrizAdj[posicoes.index(i)][posicoes.index(
                    j)] = self.dicionario[i][j]

        print("Matriz de adjacencia: ", self.matrizAdj, "\n")

    def lista_para_matrizInc(self):
        '''
        Transforma a lista de adjacencia atual em uma matriz de incidencia
        '''
        # A lista arestas possui todos os pares ordenados de vertices adjacentes, ou seja, as arestas.
        # As arestas representam as colunas em nossa matriz de incidencia
        arestas = []
        arestas.extend(self.gerar_lista_de_arestas())
        print("Arestas: ", arestas)

        #Cria uma matriz de zeros numero de vertices x numero de arestas
        self.matrizInc = [
            [0 for x in range(len(arestas))] for y in range(len(self.dicionario))]

        #lista com todos os vertices do grafo, na ordem que aparecem na lista de adjacencia
        posicoes = []
        for i in self.dicionario.keys():
            posicoes.append(i)

        # Verifica a existencia de cada vertice em cada relacao (u, v), caso exista
        # e atribuido a cada posicao da matriz o valor 1 que representa a existencia
        # da incidencia
        for i in self.dicionario.keys():
            for j in range(len(arestas)):
                if i in arestas[j]:
                    self.matrizInc[posicoes.index(i)][j] = 1
                else:
                    self.matrizInc[posicoes.index(i)][j] = 0

        print("Matriz Incidencia: ", self.matrizInc, "\n")

    def gerar_subgrafo_ind_vertices(self):
        '''
        Gera um subgrafo induzido por vertices escolhendo de forma aleatoria a quantidade
        e quais vertices a serem retirados.
        '''

        num_of_vertices = len(self.dicionario.keys())
        print("Numero de vertices: ", num_of_vertices)
        qntde_vertices_a_remover = random.randrange(0, num_of_vertices+1)
        print("Quantidade de vertices a remover: ", qntde_vertices_a_remover)

        vertices_a_remover = []
        vertices_a_remover.extend(random.sample(
            self.dicionario.keys(), qntde_vertices_a_remover))
        print("Vertices a remover: ", vertices_a_remover)

        for i in vertices_a_remover:
            self.remover_vertice(i)

        print('Lista atualizada: ', self.dicionario)

    def gerar_subgrafo_ind_arestas(self):
        '''
        Gera um subgrafo induzido por vertices escolhendo de forma aleatoria a quantidade
        e quais vertices a serem retirados.
        '''
        arestas = []
        arestas.extend(self.gerar_lista_de_arestas())
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

        print('Lista atualizada: ', self.dicionario)

    def main(self):
        # print("2 e 7 sao vizinhos?: ", self.eh_vizinho(2, 7))
        # print("Vizinhos do vertice 5: ", self.retorna_vizinhos(5))
        # self.inserir_vertice(98, 6, 12)
        # self.inserir_vertice(13, 5, 8)
        # self.inserir_vertice(9, 2, 35)
        # self.inserir_vertice_isolado(22)
        # self.inserir_aresta(1, 7, 68)
        # self.remover_vertice(6)
        # self.remover_aresta(1, 6)
        #self.deletar_grafo()
        self.lista_para_matrizAdj()
        #self.lista_para_matrizInc()
        #self.gerar_subgrafo_ind_vertices()
        #self.gerar_subgrafo_ind_arestas()


if __name__ == '__main__':
    graph = Graph()
    graph.main()
