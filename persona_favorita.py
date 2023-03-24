from package.directed_graph import DirectedGraph
from pprint import pprint 

g = {}

grafo = DirectedGraph(g)

grafo.addMultipleVertex(['Jesus', 'María', 'Pepito' , 'Chanchito', 'Ricky', 'Onix'])

grafo.addEdge('Jesus', 'María')
grafo.addEdge('María', 'Jesus')

grafo.addEdge('Chanchito', 'Pepito')
grafo.addEdge('Ricky', 'Onix')
grafo.addEdge('Onix', 'Ricky')
grafo.addEdge('Pepito', 'Onix')
grafo.addEdge('Jesus', 'Onix')

pprint(grafo.info, width=1)

print(grafo.confirmar_reunion())

# print(grafo.neighbors('Jesus'))