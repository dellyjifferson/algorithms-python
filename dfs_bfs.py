# DFS vs BFS (conceptual version)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

print("DFS order: A -> B -> D -> E -> C -> F")
print("BFS order: A -> B -> C -> D -> E -> F")
