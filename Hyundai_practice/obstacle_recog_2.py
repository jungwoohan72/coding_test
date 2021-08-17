import sys

a = 0
grid = []
for line in sys.stdin:
        if a == 0:
                n = int(line)
                a += 1
        else:
                grid.append(list(map(int, line.strip())))

def dfs(x,y):
        global temp

        if x <= -1 or x >= n or y <= -1 or y >= n:
                return
        if grid[x][y] == 1:
                temp += 1
                grid[x][y] = 0
                dfs(x-1,y)
                dfs(x,y-1)
                dfs(x+1,y)
                dfs(x,y+1)
                return True
        return False

obs = []
result = 0
for i in range(n):
        for j in range(n):
                temp = 0
                if dfs(i,j) == True:
                        result += 1
                        obs.append(temp)

print(result)
obs.sort()
for i in obs:
        print(i)