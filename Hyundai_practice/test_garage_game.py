import sys
from collections import deque

def dfs(x,y,target):
    global N, temp
    if x < 2*N or x >= 3*N or y <= -1 or y >= N:
        return False
    if temp[x][y] == target:
        temp[x][y] = 0
        dfs(x-1,y,target)
        dfs(x+1,y,target)
        dfs(x,y-1,target)
        dfs(x,y+1,target)
        return True
    return False

N = int(input())

graph = []
for _ in range(3*N):
    graph.append(list(map(int, sys.stdin.readline().split())))

sim_num = 0

temp = graph[:][:]
for i in range(2*N,3*N):
    for j in range(N):
        target = temp[i][j]
        if dfs(i,j,target) == True and target > 0:
            sim_num +=1

print(sim_num)
'''
2
1 1
2 2
1 1
3 3
4 4
1 2

15

3
8 5 1
9 6 1
10 7 1
11 1 3
12 1 3
13 1 3
1 2 2
1 2 2
1 2 2

36
'''