import time
import sys

start_time = time.time()

n, m = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

ans = 0

for i in range(n):
    ans = max(ans, min(graph[i]))

print(ans)

end_time = time.time()

print(end_time-start_time)
