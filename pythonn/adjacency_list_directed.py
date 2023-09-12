class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def adjacency_list(self):
        return self.graph

# Example usage
g = DirectedGraph()

g.add_vertex("1")
g.add_vertex("2")
g.add_vertex("3")
g.add_vertex("4")
g.add_vertex("5")
g.add_vertex("6")

#g.add_edge("1","None")
g.add_edge("2", "1")
g.add_edge("2", "4")
g.add_edge("3", "2")
g.add_edge("3", "6")
g.add_edge("4", "3")
g.add_edge("4", "5")
g.add_edge("4", "6")
g.add_edge("5", "1")
g.add_edge("6", "1")
g.add_edge("6", "2")
g.add_edge("6", "5")


adj_list = g.adjacency_list()
for vertex, edges in adj_list.items():
    if vertex=="1":
        print("Vertex 1 => [/]")
        continue   
    edges_str = ", ".join(edges)
    print(f"Vertex {vertex} => [{edges_str}] "+"[/]")
