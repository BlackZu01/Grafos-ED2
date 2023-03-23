from pprint import pprint
from vertex import Vertex
import numpy as np

class Graph:
    def __init__(self, g_dict: dict=None) -> None:
        if g_dict is None:
            self.g_dict = g_dict
        self.g_dict = g_dict
        self.adj_m = None

    @property
    def nVertex(self) -> int:
        return len(list(self.g_dict.keys()))
    
    @property
    def info(self) -> dict:
        return self.g_dict

    @property 
    def vertices(self):
        return [vertex for vertex in self.g_dict.keys()]

    def addVertex(self, data: int) -> None:
        if data not in self.g_dict.keys():
            self.g_dict[data] = list()
            return 
    
    def addEdge(self, vertex: str, edge: str) -> None:
        self.g_dict[vertex].append(edge)

    def addEdges(self, vertex: str, edges: tuple=()) -> None:
        for edge in edges:
            self.g_dict[vertex].append(edge)

    def generateAdjMat(self) -> None:
        self.adj_m = np.zeros((self.nVertex, self.nVertex), dtype=int)
        vertex = list(self.g_dict.keys())

        for k in range(self.adj_m.shape[0]):
            for j in range(self.adj_m.shape[1]):
                for i in range(len(self.g_dict[vertex[k]])):
                    if vertex[j] == self.g_dict[vertex[k]][i]:
                        self.adj_m[k][j] = 1

direc = {
    'A' : ['B'],
    'B': []
}

grafo_dir = Graph(direc)
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