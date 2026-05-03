def dfs(graph,node,visited):
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph,neighbor,visited)

graph={
    'A':['B','C','D'],
    'B':['F','E'],
    'C':['H','I'],
    'D':[],
    'F':[],
    'H':[],
    'I':[],
    'E':[]
}            

visited=set()
print("DFS traversal starting from A")
dfs(graph,'A',visited)
        