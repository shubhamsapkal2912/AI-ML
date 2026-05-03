from queue import PriorityQueue

# Best First Search Function
def best_first_search(graph, start, goal, heuristic):
    visited = set()
    pq = PriorityQueue()

    # (heuristic value, node)
    pq.put((heuristic[start], start))

    while not pq.empty():
        h, current = pq.get()

        if current == goal:
            print("Goal reached:", current)
            return

        if current not in visited:
            print(current, end=" ")
            visited.add(current)

            for neighbor in graph[current]:
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