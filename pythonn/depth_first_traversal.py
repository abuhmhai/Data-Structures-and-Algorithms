from collections import defaultdict

def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example usage
graph = defaultdict(list)
graph['A'] = ['B','S']
graph['S'] = ['C','G']
graph['C'] = ['D', 'E','F']
graph['G']=['H']


start_node = 'A'
visited = set()
print("Depth-First Traversal starting from node", start_node)
dfs(graph, start_node, visited)
