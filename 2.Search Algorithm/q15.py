from queue import PriorityQueue

# Best First Search Function
def best_first_search(graph, start, goal, heuristic):
    visited = set()
    pq = PriorityQueue()

    # (heuristic value, node)
    pq.put((heuristic[start], start))

    while not pq.empty():
        h, node = pq.get()

        if node == goal:
            print("Goal reached:", node)
            return

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    pq.put((heuristic[neighbor], neighbor))


# Example Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Heuristic values (estimate to goal)
heuristic = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 2,
    'E': 1,
    'F': 0   # Goal node has 0
}

# Run Best First Search
start = 'A'
goal = 'F'

print("Best First Search Traversal:")
best_first_search(graph, start, goal, heuristic)