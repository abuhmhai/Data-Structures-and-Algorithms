from collections import defaultdict, deque

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Example usage
graph = defaultdict(list)
graph[0] = [1, 2]
graph[1] = [0, 3, 4]
graph[2] = [0, 4]
graph[3] = [1, 5]
graph[4] = [1, 2]
graph[5] = [3]

start_node = 0
print("Breadth-First Traversal starting from node", start_node)
bfs(graph, start_node)
