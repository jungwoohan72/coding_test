import sys
import heapq

INF = 1e9
n,m,c = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = distance[now] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

count = 0
max_dist = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(d, max_distance)

print(count-1, max_distance)