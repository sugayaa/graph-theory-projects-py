import networkx as nx
import matplotlib as mlp
import matplotlib.pyplot as plt
import queue

'''
-------------------------------------------------------------------
G é o grafo
u é o índice do nó atual, na primeira chamada da função é a raíz
vis é o vetor que armazena caso um nó foi visitado ou não
pred é o vetor que armazena o nós predecessores(ou pais).
-------------------------------------------------------------------
nesse caso vis e pred são variaveis globais
-------------------------------------------------------------------
'''
def dfs(G, u, vis, pred):
    vis[u] = True

    #se desejarmos 'printar' a navegação
    #print('nó', u, 'visitado')
    for v in list(G.adj[str(u)]):
        v = int(v)
        if not vis[v]:
            pred[v] = u
            dfs(G, v, vis, pred)



'''
-------------------------------------------------------------------
s é a raíz(nó inicial)
-------------------------------------------------------------------
'''
def bfs(G, s, pred):
    #preparação
    vis = [False] * (len(G) + 1)
    q = queue.Queue()

    q.put(s)
    vis[s] = True

    while len(q) != 0:
        u = q.get()
        #caso desejarmos 'printar' a navegação
        #print('nó', u, 'visitado')

        for v in list(G.adj[str(u)]):
            v = int(v)
            if not vis[v]:

                vis[v] = True
                pred[v] = u
                q.put(v)


'''
------------------------------------------------------------------
G é o grafo base que foi percorrido
s é a raíz usada na navegação
pred é o vetor de predecessores
------------------------------------------------------------------
'''
def treeMount(G, s, pred):
    tree = nx.Graph()
    q = queue.Queue()
    ehConexo = [False] * (len(G) + 1)

    for u in list(G.nodes()):
        tree.add_node(int(u))

    q.put(s)

    while len(q) != 0:
        u = q.get()
        ehConexo = True

        for v in range(1, len(pred) + 1):
            if pred[v] == u:
                tree.add_edge(u,v)
                q.put(v)

    for v in list(G.nodes()):
        v = int(v)
        if not ehConexo[v]:
            tree.remove_node(v)


    return tree



def main():
    grafo_karate    = nx.read_pajek('karate.paj')
    grafo_dolphins  = nx.read_pajek('dolphins.paj')



    karate_pred_bfs = [-1] * (len(grafo_karate) + 1)
    karate_pred_dfs = [-1] * (len(grafo_karate) + 1)
    dolphins_pred_bfs = [-1] * len(grafo_dolphins)
    dolphins_pred_dfs = [-1] * len(grafo_dolphins)

    karate_vis_dfs = [False] * (len(grafo_karate) + 1)
    dolphins_vis_dfs = [False] * len(grafo_dolphins)
    #bfs implementa vetor de visitados dentro da função

    dfs(grafo_karate, int(list(grafo_karate.nodes())[0]), karate_vis_dfs, karate_pred_dfs)

if __name__ == "__main__":
    main()
