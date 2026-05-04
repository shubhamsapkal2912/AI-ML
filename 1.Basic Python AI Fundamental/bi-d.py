# Graph (same style as your BFS)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

def bidirectional(start, goal):

    # Two BFS queues
    q1 = [start]
    q2 = [goal]

    # Two visited sets
    v1 = set([start])
    v2 = set([goal])

    while q1 and q2:

        # Forward BFS
        node1 = q1.pop(0)
        for n in graph[node1]:
            if n not in v1:
                q1.append(n)
                v1.add(n)

            # Check meeting point
            if n in v2:
                print("Path found at:", n)
                return

        # Backward BFS
        node2 = q2.pop(0)
        for n in graph[node2]:
            if n not in v2:
                q2.append(n)
                v2.add(n)

            # Check meeting point
            if n in v1:
                print("Path found at:", n)
                return

    print("No Path Found")


# Call
bidirectional('A', 'F')