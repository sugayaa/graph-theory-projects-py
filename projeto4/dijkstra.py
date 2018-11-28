import numpy as np
import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt
import math as m
import heapq
import queue
import random

#constante representando o tamanho do grafo
TAM = 59

'''
#vetores representando respectivamente as distancias dos vértices e caso eles já foram visitados
dist = [m.inf] * TAM
vis = [False] * TAM
'''
dss = [0] * TAM
pdss = [0] * TAM

d2s = []
pd2s = []

d3s = []
pd3s = []

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

def dijkstraMultiSource(sources):
    pq = []

    dist = [m.inf] * TAM
    vis = [False] * TAM
    pred = [-1] * TAM

    for source in sources:
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

def montaGrafosAgrupamento(dist, pred, sources):
    Gs = [0] * len(sources)
    q = queue.Queue()

    for i in range(len(sources)):
        Gs[i] = nx.Graph()
        Gs[i].add_nodes_from(range(TAM))

    for i in range(len(sources)):
        q.put(sources[i])

        while not q.empty():
            curr_node = q.get()
            for j in range(len(pred)):
                if pred[j] == curr_node:
                    Gs[i].add_edge(curr_node, j)
                    q.put(j)
    return Gs

def monteGrafosAgrupamento(dist, pred, sources):
    G = nx.Graph()
    q = queue.Queue()


    G.add_nodes_from(range(TAM))

    for i in range(len(sources)):
        q.put(sources[i])

        while not q.empty():
            curr_node = q.get()
            for j in range(len(pred)):
                if pred[j] == curr_node:
                    G.add_edge(curr_node, j)
                    q.put(j)
    return G



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

random2 = random.sample(range(59), 2)
random3 = random.sample(range(59), 3)

d2s, pd2s = dijkstraMultiSource(random2)
d3s, pd3s = dijkstraMultiSource(random3)

g2s = montaGrafosAgrupamento(d2s, pd2s, random2)
g3s = montaGrafosAgrupamento(d3s, pd3s, random3)

g2 = monteGrafosAgrupamento(d2s, pd2s, random2)

options = [
        {'node_color':'red','node_size': 100, 'width': 1, 'with_labels':True, 'font_size': 6},
        {'node_color':'purple','node_size': 100, 'width': 3},
        {'node_color':'black','node_size': 100, 'width': 3}
        ]
'''
for g in range(len(g2s)):
    nx.draw(g2s[g],**options[g])

plt.subplot(121)
nx.draw(g2s[0], **options[0])
plt.subplot(122)
nx.draw(g2s[1], **options[1])
plt.subplot(111)
'''
g2 = nx.relabel_nodes(g2, nome_vertices)
nx.draw(g2, **options[0])
plt.show()
