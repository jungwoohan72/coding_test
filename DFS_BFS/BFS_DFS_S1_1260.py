import sys
from collections import deque

def BFS(graph, visited, v):
    temp = []
    q = deque([v])

    temp.append(v)
    visited[v] = True
    while q:
        start = q.popleft()

        for node in graph[start]:
            if visited[node] == False:
                temp.append(node)
                visited[node] = True
                q.append(node)
    print(' '.join([str(temp[i]) for i in range(len(temp))]))

def DFS(graph, visited, v):
    ans.append(v)
    visited[v] = True

    for node in graph[v]:
        if visited[node] == False:
            visited[node] = True
            DFS(graph, visited, node)

n, m, v = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
visited_temp = visited[:]
ans = []

for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)

for i in range(1,n+1):
    graph[i] = sorted(graph[i])

DFS(graph, visited, v)
print(' '.join([str(ans[i]) for i in range(len(ans))]))
BFS(graph, visited_temp, v)