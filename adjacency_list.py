all_edges = [
("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("C", "E"), ("D", "E" )
]


class Graph:
    def __init__(self, Nodes):
        self. nodes = Nodes
        self.adj_list = {}
        for node in self. nodes:
            self.adj_list[node] = []
    def add_edge (self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
    def degree (self, node) :
        deg= len(self.adj_list[node])
        return deg
    def print_adj_list(self):
        for node in self. nodes:
            print(node,"=>",self.adj_list[node]);

nodes=['A','B','C','D','E']
graph=Graph(nodes)
for u,v in all_edges:
    graph.add_edge(u,v)

graph.print_adj_list()
print("Degree of C", graph.degree("C"))
