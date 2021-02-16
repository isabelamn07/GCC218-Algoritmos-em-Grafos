'''
FORD-FULKERSON-METHOD.G; s; t/
1 initialize flow f to 0
2 while there exists an augmenting path p in the residual network Gf
3    augment flow f along p
4 return f

Ford-Fulkerson(G,s,t)
1 for each edge (u,v) in G.E
2   (u,v).f = 0
3 while there exists a path p from s to t in residualnetwork Gf 
4   cf = min{cf(u,v): (u, v) is in p}
5   for each edge (u,v) in p 
6       if (u, v).f = (u, v).f + cf(p)
7           (v, u).f = (v, u).f - cf(p)
8 


'''
import copy


grafo = { 0: {1: 16, 2: 13},
          1: {3: 12},
          2: {1: 4, 4: 14},
          3: {2: 9, 5: 20},
          4: {3: 7, 5: 4},
          5: {}}

source = 0
sink = 5
grafo_residual = {}
caminho = []

grafo_residual = copy.deepcopy(grafo)
print(grafo_residual)

def ford_fulkerson(G, s, t):
    flow = 0

    while caminho_aumentante():
        if caminho:
            menor = []
            for i in range(len(caminho)-1):
                menor.append(grafo_residual[caminho[i]][caminho[i+1]])
                print(menor)
            cf = min(menor)
            print('cf', cf)
            flow += cf
            for i in range(len(caminho)-1):
                grafo_residual[caminho[i]][caminho[i+1]] -= cf
        print("grafo residual", grafo_residual)
    print("flow", flow)

def caminho_aumentante():
    visitado = [source]    
    predecessor = {source: 0}
    caminho.clear()

    
    list(grafo.keys())
 
    Q = []
    Q.append(source)
    s = sink
    while Q:
        u = Q.pop(0)
        for v in grafo_residual[u]:
            if (v not in visitado) and (grafo_residual[u][v] > 0):
                visitado.append(v)
                predecessor[v] = u
                Q.append(v)
    
    print("visitado", visitado)
    print("predecessor", predecessor)
    if sink in predecessor:         
        for x in range(len(predecessor)):
            if s not in caminho:
                caminho.insert(0, s)
                s = predecessor[s]
               
    
    
    print("caminho", caminho)
    if sink in caminho:
        return True
    else:
        return False    


ford_fulkerson(grafo, source, sink)


