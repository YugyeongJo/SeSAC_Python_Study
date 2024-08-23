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
        print(type(self))
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
            
    def get_nodes(self):
        return list(self.adj_list.keys())

    def get_edges(self):
        res = []
        for from_vertex, to_vertices in self.adj_list.items():
            for to_vertex in to_vertices:
                res.append(Edge(from_vertex, to_vertex))
        return res 
            
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
        n = len(V)
        
        vertex2index = {}
        for idx, v in enumerate(V):
            vertex2index[v] = idx 
        
        matrix = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(0)
            matrix.append(row)
        
        for e in E:
            i = vertex2index[e.from_vertex]
            j = vertex2index[e.to_vertex]
            
            matrix[i][j] = 1
        
        for i in range(n):
            matrix[i][i] = 1
        
        self.matrix = matrix 
        self.vertex2index = vertex2index
        
    def get_nodes(self):
        return list(self.vertex2index.keys())
    
    def get_edges(self):
        res = []
        nodes = self.get_nodes()
        
        for i, from_vertex in enumerate(nodes):
            for j, to_vertex in enumerate(nodes):
                if i != j and self.matrix[i][j] == 1:
                    res.append(Edge(from_vertex, to_vertex))
        return res
        
    def __str__(self):
        return str(self.matrix)
    
    def __eq__(self, other):
        if isinstance(other, AdjMatrix):
            return self.matrix == other.matrix
        return False