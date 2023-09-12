class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}
    
    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]
    
    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1

def kruskal(graph,start_vertex):
    minimum_spanning_tree = []
    vertices = set()
    
    for edge in graph:
        vertices.update(edge[:2])
    
    union_find = UnionFind(vertices)
    
    sorted_edges = sorted(graph, key=lambda edge: edge[2])
    
    for edge in sorted_edges:
        vertex1, vertex2, weight = edge
        if union_find.find(vertex1) != union_find.find(vertex2):
            minimum_spanning_tree.append(edge)
            union_find.union(vertex1, vertex2)
    
    return minimum_spanning_tree

# Example usage
graph = [
    ('1', '2', 16),
    ('1', '5', 19),
    ('1', '6', 21),
    ('2', '6', 11),
    ('2', '3', 5),
    ('2', '4', 6),
    ('3', '4', 10),
    ('4', '6', 14),
    ('4', '5', 18),
    ('5', '6', 33),

]
start_vertex = '1'
minimum_spanning_tree = kruskal(graph,start_vertex)

minimum_spanning_tree_starting_from_1 = [edge for edge in minimum_spanning_tree if edge[0] == start_vertex]

# Print the remaining edges in the order they were added to the minimum spanning tree
print("Minium spanning tree starting from", start_vertex)
for edge in minimum_spanning_tree:
    if edge in minimum_spanning_tree_starting_from_1:
        print(edge[0], "-", edge[1], ":", edge[2])


for edge in minimum_spanning_tree:
    if edge[0] != '1' and edge[1] != '1':
        print(edge[0], "-", edge[1], ":", edge[2])

