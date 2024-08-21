class Vertex:
    def __init__(self, node_id, datum):
        self.datum = datum 
        self.node_id = node_id 

    def __eq__(self, other):
        if isinstance(self, Vertex) and isinstance(other, Vertex):
            return self.node_id == other.node_id
        return False 

    def __hash__(self):
        return hash((self.node_id, self.datum))

    def __str__(self):
        return str(self.datum)
    
    # 딕셔너리나 리스트안에서 print()
    def __repr__(self):
        return self.__str__()

class Edge:
    def __init__(self, from_vertex, to_vertex, is_directed = True, **data):
        assert isinstance(from_vertex, Vertex)    
        self.from_vertex = from_vertex

        assert isinstance(to_vertex, Vertex)
        self.to_vertex = to_vertex

        self.is_directed = is_directed
        self.data = data 
    
    def __eq__(self, other):
        if isinstance(self, Edge) and isinstance(other, Edge):
            return self.from_vertex == other.from_vertex and self.to_vertex == other.to_vertex
    
    def __str__(self):
        return f'{self.from_vertex} -> {self.to_vertex}'
    
    # 딕셔너리나 리스트안에서 print()
    def __repr__(self):
        return self.__str__()


class AdjList:
    def __init__(self, V, E):
        for v in V:
            assert isinstance(v, Vertex)    
        self.adj_list = {v: [] for v in V}
        
        for edge in E:
            self.adj_list[edge.from_vertex].append(edge.to_vertex)
            
    def add_vertex(self, v):
        assert v not in self.adj_list
        self.adj_list[v] = []
    
    def __str__(self):
        return str(self.adj_list)
    
    def __eq__(self, other):
        if isinstance(other, AdjList):
            return self.adj_list == other.adj_list
        return False

class AdjMatrix:
    def __init__(self, V, E):
        pass 