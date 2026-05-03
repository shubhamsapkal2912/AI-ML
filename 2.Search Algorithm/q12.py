from collections import deque

# BFS function
def breadth_first_search(graph, start):
    visited = set()        # To keep track of visited nodes
    queue = deque()        # Queue for BFS

    visited.add(start)
    queue.append(start)

    print("BFS Traversal:")

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        # Visit all neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# Example graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Start BFS from node 'A'
breadth_first_search(graph, 'A')