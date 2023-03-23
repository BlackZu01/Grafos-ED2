import numpy as np

class DirectedGraph:
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
        raise ValueError('The vertex is already in the Graph')
    
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