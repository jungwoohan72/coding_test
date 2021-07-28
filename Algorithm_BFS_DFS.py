from collections import deque

def DFS(graph, start, visited):
    visited[start] = True

    for node in graph[start]:
        if not visited[node]:
            print(node)
            DFS(graph, node, visited)


def BFS(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for node in graph[v]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True
                print(node)


n = 8  # total number of nodes
visited = [False] * (n + 1)
v = 1

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# DFS(graph,v,visited)
BFS(graph, v, visited)