##Básico
import networkx as nx
import matplotlib.pyplot as plt


#Criando um grafo
G = nx.Graph()

##Vertices
##Adicionando um único vertice
G.add_node(1)

#Adicionaod uma lista de vertices
G.add_nodes_from([2, 3])

##Adicionando um intervalo de vertices
H = nx.path_graph(10)
G.add_nodes_from(H)

'''nx.draw(G, with_labels=True, font_weight='bold')
plt.show()'''

## Arestas
#Adicionando um aresta por vez
G.add_edge(1, 2)
e = (2, 3)
G.add_edge(*e) #unpack edge tuple *

## Adding a list of edges:
G.add_edges_from([(1, 2), (1, 3)])

## or by adding any ebunch of edges.l An ebunch is any iterable container of edge-tubpes. An edge-tupçe can be 
# a 2-tuple of nodes or a 3-tupla with 2 nodes followed by an edge attribute dicionary, e.g., (2, 3, {'weight': 3.1415}).
G.add_edges_from(H.edges)
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()

## Limpar

G.clear()

G.add_edges_from([(1,2), (1, 3)])
G.add_node(1)
G.add_edge(1, 2)
G.add_node("spam") ## adds node "spam"
G.add_nodes_from("spam") # adds 4 nodes: 's', 'p', 'a', 'm'
G.add_edge(3, 'm')

G.number_of_nodes()
G.number_of_edges()

print(list(G.nodes))
print(list(G.edges))
print(list(G.adj[1]))  # or list(G.neighbors(1))
print(G.degree[1]) # the number of edges incident to 1

## One can specify to report the edges and degree from a subset of all nodes using an nbunch. An
# nbunch is any of: None (meaning all nodes), a node, or an iterable container of nodes that is not
# itself a node in the graph.
print(G.edges([2, 'm']))
print(G.degree([2, 3]))


## One can remove nodes and edges from the graph in a similar fashion to adding. Use methods
# Graph.remove_node()
# Graph.remove_nodes_from()
# Graph.remove_edge()
# Graph.remove_edges_from()

G.remove_node(2)
G.remove_nodes_from("spam")
print(list(G.nodes))
G.remove_edge(1, 3)

## When creating a graph structure by instantiating one of the graph classes you can specify data in several formats.
G.add_edge(1, 2)
H = nx.DiGraph(G) # creating a DiGraph using the connections from G
print(list(H.edges()))
edgelist = [(0, 1), (1, 2), (2, 3)]
H = nx.Graph(edgelist)

## What to use as nodes and edges
# You might notice that nodes and edges are not specified as NetworkdX objects. This leaves you free
# to use meaningful items as nodes and edges. The most common choices are numbers or strings, but a node 
# can be any hashable object (except none), and an edge can be associated with any object x using
# G.add_edge(n1, n2, object=x).
