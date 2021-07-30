import sys

def DFS(x,y):
    if graph[y][x] == 'W':

    else:

n, m = map(int, sys.stdin.readline().split())

graph = []

for _ in range(m):
    graph.append(list(sys.stdin.readline().rstrip()))
