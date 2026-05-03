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

    for n in graph[node]:
        if n not in visited:
            depth_first_search(n, visited)

# Function call
print("DFS Traversal:")
visited = set()
depth_first_search('5', visited)