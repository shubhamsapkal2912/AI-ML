from collections import deque

# Function to perform Bidirectional Search
def bidirectional_search(graph, start, goal):
    
    if start == goal:
        return [start]
    
    # Initialize forward and backward queues
    forward_queue = deque([start])
    backward_queue = deque([goal])
    
    # Visited dictionaries
    forward_visited = {start: None}
    backward_visited = {goal: None}
    
    # Function to construct path
    def construct_path(meeting_node):
        path = []
        
        # From start to meeting node
        node = meeting_node
        while node is not None:
            path.append(node)
            node = forward_visited[node]
        path.reverse()
        
        # From meeting node to goal
        node = backward_visited[meeting_node]
        while node is not None:
            path.append(node)
            node = backward_visited[node]
        
        return path
    
    # Search loop
    while forward_queue and backward_queue:
        
        # Expand forward
        current_forward = forward_queue.popleft()
        
        for neighbor in graph[current_forward]:
            if neighbor not in forward_visited:
                forward_queue.append(neighbor)
                forward_visited[neighbor] = current_forward
                
                if neighbor in backward_visited:
                    return construct_path(neighbor)
        
        # Expand backward
        current_backward = backward_queue.popleft()
        
        for neighbor in graph[current_backward]:
            if neighbor not in backward_visited:
                backward_queue.append(neighbor)
                backward_visited[neighbor] = current_backward
                
                if neighbor in forward_visited:
                    return construct_path(neighbor)
    
    return None  # No path found


# ==========================================
# Example Graph (Undirected)
# ==========================================
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['F']
}

# ==========================================
# Driver Code
# ==========================================
start_node = 'A'
goal_node = 'G'

path = bidirectional_search(graph, start_node, goal_node)

# Output
if path:
    print("Path found:", " -> ".join(path))
else:
    print("No path exists between", start_node, "and", goal_node)