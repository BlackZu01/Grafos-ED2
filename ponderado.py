from package.ponderado_directed import GrafoPonderado

graf = {

}

grafo = GrafoPonderado(graf)

grafo.addVertex('A')
grafo.addVertex('B')
grafo.addVertex('C')
grafo.addVertex('D')
grafo.addVertex('E')
grafo.addVertex('F')

grafo.addEdge('B', 'A', 1)
grafo.addEdge('A', 'C', 2)
grafo.addEdge('C', 'E', 3)
grafo.addEdge('D', 'B', 2)
grafo.addEdge('D', 'F', 7)
grafo.addEdge('F', 'E', 1)

##Segundo las internas

grafo.addEdge('C', 'B', 1)
grafo.addEdge('B', 'E', 3)
grafo.addEdge('E', 'D', 2)
grafo.addEdge('C', 'D', 4)

for i in grafo.g_dict.keys():
    for j in grafo.g_dict.keys():
        minimo, camino = grafo.dijkstra(i, j)
        print(f'\nCosto mínimo para llegar de {i} a {j}: {minimo}')  
        print(f'Camino mínimo tomado para llegar de {i} a {j}: {" -> ".join(camino)}')