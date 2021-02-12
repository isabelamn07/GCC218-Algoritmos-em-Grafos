from math import inf

'''
BELLMAN-FORD(G, w, s)
1 INITIALIZE-SINGLE-SOURCE(G, s)
2 for i = 1 to |G.V| - 1
3   for each edge (u, v) pertence a G:E
4       RELAX(u, v, w)
5   for each edge (u, v) pertence a G:E
6       if v.d => u.d + w(u, v)
7           return FALSE
8 return TRUE

INITIALIZE-SINGLE-SOURCE(G, s)
1 for each vertex v pertence a G.V
2   v.d = inf 
3   v.pi = NIL
4 s.d = 0

RELAX(u, v, w)
1 if v.d > u.d + w(u, v)
2   v.d = u.d + w(u,v)
3   v.pi = u

'''
single_source = []
def bellman_ford(grafo_bf):
    vertices = list(grafo_bf.keys())
    for i in grafo.keys():
        single_source.append([i, inf, None])

    single_source[0][1] = 0

    print("Single source: ", single_source)
    for i in range(0, len(grafo.keys())-1):
        print("Iteracao: ", i)
        for x in grafo.keys():
            for y in grafo[x]:
                print("Aresta: ", (x, y))
                relax(x, y)
    for i in grafo_bf.keys():
        for j in grafo_bf[i]:
            if single_source[vertices.index(j)][1] > single_source[vertices.index(i)][1] + grafo_bf[i][j]:
                return False
    return True
              
    

def relax(u, v):
    if single_source[vertices.index(v)][1] > \
        single_source[vertices.index(u)][1] + grafo[u][v]:
        single_source[vertices.index(
            v)][1] = single_source[vertices.index(u)][1] + grafo[u][v]
        single_source[vertices.index(
            v)][2] = u

        print(single_source)
       

'''RELAX(u, v, w)
1 if v.d > u.d + w(u, v)
2   v.d = u.d + w(u, v)
3   v.pi = u'''

grafo = {'s':{'t':6, 'y':7},
         't':{'x':5, 'y':8, 'z':-4},
         'x':{'t':-2},
         'y':{'x': -3, 'z':9},
         'z':{'s':2, 'x': 7}         
         }
vertices = list(grafo.keys())
print(bellman_ford(grafo))
