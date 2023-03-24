from package.directed_graph import DirectedGraph
from pprint import pprint

direc = {
}

grafo_dir = DirectedGraph(direc)
grafo_dir.addVertex('Algoritmia I')
grafo_dir.addVertex('Cálculo I')
grafo_dir.addVertex('Algoritmia II')
grafo_dir.addVertex('Cálculo II')

grafo_dir.addEdge('Algoritmia I', 'Algoritmia II')
grafo_dir.addEdge('Cálculo I', 'Cálculo II')
grafo_dir.addEdge('Algoritmia II', 'Algoritmia I')


# print('\n\t[+] Grafo dirigido [+]\n')
# pprint(grafo_dir.info, width=1)
# grafo_dir.generateAdjMat()

# print('\n\t[+] Matriz de adyacencia [+]\n')
# pprint(grafo_dir.adj_m, width=1)

# print(grafo_dir.DFS('M', 'S', []))

# print(grafo_dir.tiene_ciclo())

if grafo_dir.tiene_ciclo():
    print('No es posible que haya ciclos en las materias!')