from package.undirected_graph import UndirectedGraph
from pprint import pprint

graf = {
    'A': [],
}

grafo = UndirectedGraph(graf)
grafo.addVertex('C')
grafo.addVertex('B')
grafo.addVertex('D')

grafo.addEdge('A', 'C')
grafo.addEdge('B', 'D')

pprint(grafo.info, width=1)

grafo.generateAdjMat()

pprint(grafo.adj_m)