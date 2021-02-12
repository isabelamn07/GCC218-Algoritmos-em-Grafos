'''
FLOYD-WARSHALL(W)
1 n = W.rows
2 D^(0) = W
3 for k = 1 to n
4   let D^(k) = (d(ij)^(k) be a new n x n matrix
5   for i = 1 to n
6       for j = 1 to n
7           d(ij)^(k) = min(d(ij)^(k-1), d(ik)^(k) + d(km)^(k-1)
8 return D^(n)
'''
from math import inf
def floyd_warshall(grafo):
    n = len(grafo)
    D = []
    pi = []
    for i in range(len(grafo)):
        D.append([])
        for j in range(len(grafo)):
            if i == j:
                D[i].append(0)
            elif grafo[i][j] == 0:
                D[i].append(inf)
            else:
                D[i].append(grafo[i][j])
    print(D)

    for i in range(len(grafo)):
        pi.append([])
        for j in range(len(grafo)):
            if grafo[i][j] == 0 or grafo[i][j] == inf:
                pi[i].append(None)
            else:
                pi[i].append(i+1)
    #print(pi)

    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if D[i][j] <= (D[i][k] + D[k][j]):
                    pi[i][j] = pi[i][j]
                elif D[i][j] > (D[i][k] + D[k][j]):
                    pi[i][j] = pi[k][j]
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
        print(D)
    #print(D)
    print(pi)


grafo_lista = {0: {1: 3, 2: 8, 4: -4 },
         1: {3: 1, 4: 7},
         2: {1: 4},
         3: {0: 2, 2:-5},
         4: {3: 6}
}

grafo_madj = [[0, 3, 8, 0, -4],
             [0, 0, 0, 1, 7],
             [0, 4, 0, 0, 0],
             [2, 0, -5, 0, 0],
             [0, 0, 0, 6, 0]   
            ]
floyd_warshall(grafo_madj)
