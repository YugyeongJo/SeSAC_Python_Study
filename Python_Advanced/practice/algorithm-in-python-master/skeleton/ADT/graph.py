import sys 
sys.path.append('../data_structure')

try:
    from graph_datastructure import AdjList, AdjMatrix, Vertex, Edge
except ModuleNotFoundError:
    from data_structure.graph_datastructure import AdjList, AdjMatrix, Vertex, Edge


class Graph:
    def __init__(self, V, E, backend = 'VE'):
        self.backend = backend
        
        for v in V:
            assert isinstance(v, Vertex) 
        for e in E:
            assert isinstance(e, Edge)
            assert e.from_vertex in V 
            assert e.to_vertex in V 
        self.V = V 
        self.E = E
            
        if backend == 'VE':
            pass
            
        elif backend == 'adjacent_list':
            self.adj_list = AdjList(V, E)
        
        elif backend == 'adjacnet_matrix':
            self.matrix = AdjMatrix(V, E)

    def add_vertex(self, v):
        assert isinstance(v, Vertex)
        
        if self.backend == 'VE':
            self.V.append(v)
        
        elif self.backend == 'adjacent_list':
            assert v not in self.adj_list.adj_list  
            
            if v not in self.adj_list.adj_list:
                self.adj_list.add_vertex(v)
                
            if v not in self.V:
                self.V.append(v)
        
        elif self.backend == 'adjacnet_matrix':
            assert v not in self.matrix.vertex2index
            
            if v not in self.matrix.vertex2index:
                idx = len(self.matrix.vertex2index)
                
                # vertex2index에 추가된 v 추가해주기
                self.matrix.vertex2index[v] = idx
                
                # matrix에 모든 행의 마지막 열에 0 1개씩 넣어주기
                for row in self.matrix.matrix:
                    row.append(0)
                
                # matrix에 v의 행 추가해서 모든 값에 0 넣어주기
                add_row = [0] * (idx+1)
                self.matrix.matrix.append(add_row)
                
                self.matrix.matrix[idx][idx] = 1
                
    def remove_vertex(self, v):
        assert isinstance(v, Vertex)
        
        if self.backend == 'VE':
            edges_to_remove = [e for e in self.E if e.from_vertex == v or e.to_vertex == v]
            for e in edges_to_remove:
                self.remove_edge(e)
            self.V.remove(v)
        
        elif self.backend == 'adjacent_list':
            # adj_list에서 v를 value로 가진 값들을 먼저 삭제(간선 먼저 삭제)
            for neighbors in self.adj_list.adj_list.values():
                if v in neighbors:
                    neighbors.remove(v)
                    
            # 간선 모두 삭제한 뒤 최종적으로 v 정점 삭제
            if v in self.adj_list.adj_list:
                del self.adj_list.adj_list[v]
        
        elif self.backend == 'adjacnet_matrix':
            pass

    def add_edge(self, e):
        assert isinstance(e, Edge)
        
        
        if self.backend == 'VE':
            assert e.from_vertex in V
            assert e.to_vertex in V
            self.E.append(e)
        
        elif self.backend == 'adjacent_list':
            # 출발 정점이 인접 리스트에 없는 경우, 정점을 추가
            if e.from_vertex not in self.adj_list.adj_list:
                self.adj_list.add_vertex(e.from_vertex)
            
            # 도착 정점이 인접 리스트에 없는 경우, 정점을 추가
            if e.to_vertex not in self.adj_list.adj_list:
                self.adj_list.add_vertex(e.to_vertex)
            
            # 출발 정점의 인접 리스트에 도착 정점을 추가
            
            if e not in self.E:
                self.E.append(e)
        
        elif self.backend == 'adjacnet_matrix':
            assert e.from_vertex in self.matrix.vertex2index and e.to_vertex in self.matrix.vertex2index
            
            # 행과 열의 위치를 찾아서 해당 부분을 1로 변경해주기
            row_idx = self.matrix.vertex2index[e.from_vertex]
            col_idx = self.matrix.vertex2index[e.to_vertex]
            
            # import code 
            # code.interact(local = locals())
            
            self.matrix.matrix[row_idx][col_idx] = 1

    def remove_edge(self, e):
        assert isinstance(e, Edge)
        
        if self.backend == 'VE':
            self.E.remove(e)
        
        elif self.backend == 'adjacent_list':
            # from_vertex는 key와 to_vertices는 value와 모두 같으면 삭제
            from_vertex = e.from_vertex
            to_vertex = e.to_vertex
            
            for tv in self.adj_list.adj_list[from_vertex]:
                if tv == to_vertex:
                    self.adj_list.adj_list[from_vertex].remove(tv)
            
        elif self.backend == 'adjacnet_matrix':
            pass

    def get_vertices(self):
        
        if self.backend == 'VE':
            return self.V
        
        elif self.backend == 'adjacent_list':
            return list(self.adj_list.adj_list.keys()) 
        
        elif self.backend == 'adjacnet_matrix':
            pass
        
        return [] 
    
    def get_edges(self):
        
        if self.backend == 'VE':
            return self.E
        
        elif self.backend == 'adjacent_list':
            edges = []
            for from_vertex, to_vertices in self.adj_list.adj_list.items():
                for to_vertex in to_vertices:
                    edges.append(Edge(from_vertex, to_vertex))
            return edges
        
        elif self.backend == 'adjacnet_matrix':
            pass
        
        return []

    def get_neighbors(self, v):
        assert isinstance(v, Vertex)
        
        if self.backend == 'VE':
            return [e.to_vertex for e in self.E if e.from_vertex == v]
        
        elif self.backend == 'adjacent_list':
            if v in self.adj_list.adj_list:
                return self.adj_list.adj_list[v]
        
        elif self.backend == 'adjacnet_matrix':
            pass
        
        return [] 

    def dfs(self, src):
        assert isinstance(src, Vertex)
        
        visited = []
        stack = [src]
        
        while stack:
            v = stack.pop()
            if v not in visited:
                visited.append(v)
                yield v
                
                neighbors = self.get_neighbors(v)
                stack.extend(neighbors)
                
        return visited

    def bfs(self, src):
        assert isinstance(src, Vertex) 
        
        visited = []
        queue = [src]
        
        while queue:
            v = queue.pop(0)
            if v not in visited:
                visited.append(v)
                yield v
                
                neighbors = self.get_neighbors(v)
                queue.extend(neighbors)
                
        return visited 

    # Do not modify this method

    @staticmethod
    def spring_layout(nodes, edges, iterations=50, k=0.1, repulsion=0.01):
        import numpy as np
        # Initialize positions randomly
        positions = {node: np.random.rand(2) for node in nodes}
        
        for _ in range(iterations):
            forces = {node: np.zeros(2) for node in nodes}
            
            # Repulsive forces between all pairs of nodes
            for i, node1 in enumerate(nodes):
                for j, node2 in enumerate(nodes):
                    if i != j:
                        diff = positions[node1] - positions[node2]
                        dist = np.linalg.norm(diff)
                        if dist > 0:
                            forces[node1] += (diff / dist) * repulsion / dist**2
            
            # Attractive forces for connected nodes
            for edge in edges:
                node1, node2 = edge.from_vertex, edge.to_vertex
                diff = positions[node2] - positions[node1]
                dist = np.linalg.norm(diff)
                
                if dist > 0:
                    force = k * (dist - 1)  # spring force
                    forces[node1] += force * (diff / dist)
                    forces[node2] -= force * (diff / dist)
            
            # Update positions
            for node in nodes:
                positions[node] += forces[node]
        
        return positions

    def show(self):
        import matplotlib.pyplot as plt
        if self.backend == 'VE':
            nodes = self.V 
            edges = self.E 
        elif self.backend == 'adjacent_list':
            nodes = self.adj_list.get_nodes()
            edges = self.adj_list.get_edges()
        elif self.backend == 'adjacent_matrix':
            nodes = self.matrix.get_nodes()
            edges = self.matrix.get_edges()
            
        positions = Graph.spring_layout(nodes, edges)
        plt.figure(figsize=(8, 6))
        ax = plt.gca()

        # Plot nodes
        for node, pos in positions.items():
            ax.scatter(*pos, s=2000, color='lightblue')
            ax.text(*pos, node, fontsize=20, ha='center', va='center')

        # Plot edges
        for edge in edges:
            node1, node2 = edge.from_vertex, edge.to_vertex
            x_values = [positions[node1][0], positions[node2][0]]
            y_values = [positions[node1][1], positions[node2][1]]
            ax.plot(x_values, y_values, color='gray', linewidth=2)

        ax.set_title("Graph Visualization with Spring Layout", fontsize=20)
        ax.set_xticks([])
        ax.set_yticks([])
        plt.show()


if __name__ == '__main__':
    v1 = Vertex(0, 1)
    v2 = Vertex(1, 2)
    v3 = Vertex(2, 3)
    v4 = Vertex(3, 4)
    v5 = Vertex(4, 5)

    e1 = Edge(v1, v2) 
    e2 = Edge(v1, v3) 
    e3 = Edge(v2, v3)
    e4 = Edge(v2, v4)
    e5 = Edge(v3, v5) 
    e6 = Edge(v4, v5)

    V = [v1, v2]
    E = [e1]

    # g1 = Graph(V, E)
    # g1 = Graph(V, E, backend='adjacent_list')
    g1 = Graph(V, E, backend='adjacnet_matrix')
    
    # print("matrix nodes : ", g1.matrix.vertex2index)
    g1.add_vertex(v3)
    g1.add_vertex(v4)
    g1.add_vertex(v5)
    # print("matrix nodes after add_vertex : ", g1.matrix.vertex2index)

    g1.add_edge(e2)
    g1.add_edge(e3)
    g1.add_edge(e4)
    g1.add_edge(e5)
    g1.add_edge(e6)

    # print(g1.matrix)
    # print("matrix nodes after add_edge : ", g1.matrix.vertex2index)
    # print(g1.adj_list)
    # g1.show()
    
    # g1.remove_vertex(v1)
    # g1.remove_edge(e1)
    # g1.remove_edge(e2)
    # g1.remove_edge(e3)
    # g1.remove_edge(e4)
    # g1.remove_edge(e5)
    # g1.remove_edge(e6)
    # print(g1.adj_list)
    # g1.show()
    
    # print(g1.get_vertices())
    # print(g1.get_edges())
    # print(g1.get_neighbors(v1))
    
    # print("DFS:")
    # for vertex in g1.dfs(v1):
    #     print(vertex)
    
    # print("BFS:")
    # for vertex in g1.bfs(v1):
    #     print(vertex)
    
    # 질문 정리
    # 1) 시각화 구현이 왜 안되는걸까요....
    # 2) 행열 add함수는 이렇게 되면 되는건지 확인 

