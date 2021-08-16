import heapq
import sys
from collections import deque

####################### Shortest_path #######################
INF = int(1e9)

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))

    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + 1

            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

dijkstra(x)

count = 0
for i in range(len(distance)):
    if distance[i] == k:
        count += 1
        print(i)

if count == 0:
    print(-1)

####################### BFS ####################### Runtime error
'''
N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    v, e = map(int, input().split())
    graph[v].append(e)

q = deque([X])
distance = [-1]*(N+1)
distance[X] = 0

while q:
    curr = q.popleft()
    for node in graph[curr]:
        if distance[node] == -1:
            q.append(node)
            distance[node] = distance[curr]+1

is_nan = 0
for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        is_nan = 1

if is_nan == 0:
    print(-1)
'''
