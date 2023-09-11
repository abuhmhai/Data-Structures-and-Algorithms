class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.vertex_indices = {}  # To map vertex names to indices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_vertex(self, vertex):
        if vertex not in self.vertex_indices:
            index = len(self.vertex_indices)
            self.vertex_indices[vertex] = index

    def add_edge(self, u, v, w):
        u_index = self.vertex_indices[u]
        v_index = self.vertex_indices[v]
        self.graph[u_index][v_index] = w
        self.graph[v_index][u_index] = w

    def adjacency_matrix(self):
        return self.graph

# Example usage
g = Graph(6)
g.add_vertex("1")
g.add_vertex("2")
g.add_vertex("3")
g.add_vertex("4")
g.add_vertex("5")
g.add_vertex("6")

g.add_edge("1", "1", 0)
g.add_edge("2", "1", 1)
g.add_edge("2", "4", 1)
g.add_edge("3", "2", 1)
g.add_edge("3", "6", 1)
g.add_edge("4", "3", 1)
g.add_edge("4", "5", 1)
g.add_edge("4", "6", 1)
g.add_edge("5","1",1)
g.add_edge("6","1",1)
g.add_edge("6","2",1)
g.add_edge("6","5",1)
adj_matrix = g.adjacency_matrix()
for row in adj_matrix:
    print(row)
