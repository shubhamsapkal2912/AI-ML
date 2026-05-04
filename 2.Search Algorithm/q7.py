graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': [],
    '8': ['10', '20'],
    '10': [],
    '20': []
}

def depth_first_search(node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            depth_first_search(neighbor, visited)

# Function call
print("DFS Traversal:")
visited = set()
depth_first_search('5', visited)