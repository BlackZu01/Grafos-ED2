from .directed_graph import DirectedGraph

class UndirectedGraph(DirectedGraph):
    def addEdge(self, vertex: str, edge: str) -> None:
        is_in = (vertex not in self.g_dict.keys()) or (edge not in self.g_dict.keys())

        if is_in:
            raise KeyError('The two vertex must be in the graph')
        self.g_dict[vertex].append(edge)
        self.g_dict[edge].append(vertex)

    def DFS(self, start: str):
        ...
