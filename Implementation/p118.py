n, m = map(int, input().split())
i,j,k = map(int, input().split())

graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))

curr = k # currently facing direction

dx = [-1,0,1,0]
dy = [0,-1,0,1]

total_turn = 0
ans = 1


def turn_left():
    global curr
    curr = curr - 1
    if curr == -1:
        curr = 3


graph[j][i] = 1

while True:
    if j+dy[curr] < 0 or j+dy[curr] > n or i+dx[curr] < 0 or i+dx[curr] > m:
        turn_left()
        total_turn += 1
        continue

    try:
        if graph[j + dy[curr]][i + dx[curr]] == 0:
            ans += 1
            graph[j + dy[curr]][i + dx[curr]] = 1
            i = i + dx[curr]
            j = j + dy[curr]
            turn_left()
            total_turn = 0
        else:
            turn_left()
            total_turn += 1

    except IndexError:
        turn_left()
        total_turn += 1

    if total_turn == 4:
        if graph[j - dx[curr]][i + dy[curr]] == 1:
            break
        else:
            i = i + dy[curr]
            j = j - dx[curr]
            total_turn = 0

print(ans)