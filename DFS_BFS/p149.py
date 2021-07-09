# 1st line: n x m grid map 
n,m = map(int, input().split())

# 2nd line: 0 1 binary map 
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# Algorithm

def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

num = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            num += 1

print(num)