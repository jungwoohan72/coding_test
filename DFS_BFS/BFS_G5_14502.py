import sys

def diffusion(x,y):
    global graph, temp
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    for i in range(4): # for loop이 다 돌아야되므로 중간에 return 해주면 안됨.
        nx = x+dx[i]
        ny = y+dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                diffusion(nx, ny)

def fence():
    global count, graph, temp, ans

    if count == 3:
        score = 0
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j] # cloning

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    diffusion(i, j)

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 0:
                    score += 1
        ans = max(ans, score)
        return

############################ very clever ############################
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                fence()
                graph[i][j] = 0 # key point
                count -= 1
############################ very clever ############################

n, m = map(int, sys.stdin.readline().split())
count = 0
ans = 0

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

temp = [[0]*m for _ in range(n)]
fence()
print(ans)