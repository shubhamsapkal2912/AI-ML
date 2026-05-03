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

def dfs(node, visited):
    visited.add(node)
    print(node, end=" ")

    for n in graph[node]:
        if n not in visited:
            dfs(n, visited)

# Function call
print("DFS Traversal:")
visited = set()
dfs('5', visited)