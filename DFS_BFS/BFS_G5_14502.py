def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 2
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

first = 0
second = 0
third = 0
count = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            count += 1

