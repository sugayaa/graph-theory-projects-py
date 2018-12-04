import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import math
import heapq as hpq

def primMST(source):
    pq = []
    chave = [math.inf] * len(G)
    pred = [-1] * len(G)
    inMST = []

    chave[source] = 0
    hpq.heappush(pq, (0, source))

    while len(pq) != 0:
        u = hpq.heappop(pq)[1]
        inMST.append(u)

        for neighbors in G.adj[u]:
            v = neighbors
            w = G.adj[u][v]['weight']

            if v not in inMST and chave[v] > w:
                chave[v] = w
                hpq.heappush(pq, (chave[v], v))
                pred[v] = u

    return sum(chave)


m = np.loadtxt('ha30_dist.txt')
G = nx.from_numpy_matrix(m)

with open ('ha30_name.txt') as arq:
    leitura = arq.readlines()

cidades = []
vertices = G.nodes()
nome_vertices = {}
'''
for v in vertices:
    nome_vertices[v] = cidades[v]
'''
#G = nx.relabel_nodes(G, nome_vertices)

print(primMST(0))
