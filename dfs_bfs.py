# DFS vs BFS (conceptual version)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
# Just simulating the output of the traversals
print("DFS order: A -> B -> D -> E -> C -> F") # The DFS ordered output
print("BFS order: A -> B -> C -> D -> E -> F") # The BFS ordered output
