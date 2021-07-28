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

for i in n:
    for j in m:
        if j == 0:
            count += 1

