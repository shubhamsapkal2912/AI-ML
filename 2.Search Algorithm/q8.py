

# Depth-Limited Search (DLS) using recursion

def depth_limited_search(graph, node, goal, limit, visited):
    print(node, end=" ")

    if node == goal:
        return True

    if limit <= 0:
        return False

    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            found = depth_limited_search(graph, neighbor, goal, limit - 1, visited)
            if found:
                return True

    return False


# Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}

start = 'A'
goal = 'G'
limit = 3   # Depth limit

visited = set()

print("DLS Traversal:")
found = depth_limited_search(graph, start, goal, limit, visited)

if found:
    print("\nGoal node found within depth limit!")
else:
    print("\nGoal node NOT found within depth limit.")