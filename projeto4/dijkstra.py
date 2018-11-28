import numpy as np
import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt
import math as m
import heapq

#constante representando o tamanho do grafo
TAM = 59

'''
#vetores representando respectivamente as distancias dos vértices e caso eles já foram visitados
dist = [m.inf] * TAM
vis = [False] * TAM
'''
dss = [0] * TAM
pdss = [0] * TAM

def dijkstraSingleSource(source):
    pq = []

    dist = [m.inf] * TAM
    vis = [False] * TAM
    pred = [-1] * TAM

    heapq.heappush(pq, (0 ,source))
    dist[source] = 0

    #laço principal
    while len(pq) != 0:

        #recebe indice do nó atual que olharemos (current node)
        curr_node = heapq.heappop(pq)[1]

        #caso ñ foi visitado, prossegue
        if not vis[curr_node]:

            #marca como visitado
            vis[curr_node] = True

            #percorrendo lista de adjacencia do nó atual
            for neighbors in G.adj[curr_node]:
                #recebe vértice a quem o atual se liga (next node)
                next_node   = neighbors
                #recebe peso da aresta que liga curr_node -w-> next_node
                w           = G.adj[curr_node][next_node]['weight']

                #relax
                if dist[next_node] > dist[curr_node] + w:
                    pred[next_node] = curr_node
                    #print('Relax!')
                    dist[next_node] = dist[curr_node] + w
                    heapq.heappush(pq, (dist[next_node], next_node))
    return dist, pred


matriz = np.loadtxt('wg59_dist.txt')
G = nx.from_numpy_matrix(matriz)

with open ('wg59_name.txt') as arq:
    leitura = arq.readlines()

cidades = []
for x in leitura:
    if "#" not in x:
        cidades.append(x.strip())

vertices = G.nodes()
nome_vertices = {}

for v in vertices:
    nome_vertices[v] = cidades[v]


#G = nx.relabel_nodes(G, nome_vertices)
for v in range(TAM):
    dss[v], pdss[v] = dijkstraSingleSource(v)
print(pdss[0][4])
print('distancia ate vertice 1: ',dss[0][1])
