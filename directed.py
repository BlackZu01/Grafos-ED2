from package.directed_graph import DirectedGraph
from pprint import pprint

direc = {
    'A' : ['B'],
    'B': []
}

grafo_dir = DirectedGraph(direc)
grafo_dir.addVertex('C')
grafo_dir.addVertex('M')
grafo_dir.addVertex('S')

grafo_dir.addEdge('A', 'C')
grafo_dir.addEdge('S', 'A')

grafo_dir.addEdges('B', ('M', 'S'))
grafo_dir.addEdges('M', ('A', 'B'))

print('\n\t[+] Grafo dirigido [+]\n')
pprint(grafo_dir.info, width=1)
# grafo_dir.generateAdjMat()

# print('\n\t[+] Matriz de adyacencia [+]\n')
# pprint(grafo_dir.adj_m, width=1)