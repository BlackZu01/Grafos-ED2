# Clase vertice

class Vertex:
    def __init__(self, data: int) -> None:
        self.data = data 
        self.adj = list()
    
    def __repr__(self) -> str:
        return f'{self.data}'