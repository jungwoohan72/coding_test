import sys

N, K = list(map(int, input().split()))

array = []
for _ in range(K):
    array.append([])

for _ in range(N):
    x, y, k = list(map(int, sys.stdin.readline().split()))
    array[k - 1].append((x, y))

ans = int(1e9)
temp = 0
num_point = 0

for i in range(K):
    for j in range(K):
        if i == j:
            continue
        for point_i in array[i]:
            for point_j in array[j]:
                if point_i[0] == point_j[0] or point_i[1] == point_j[1]:
                    temp = (max(point_i[0], point_j[0]), min(point_i[0], point_j[0]), max(point_i[1], point_j[1]),
                            min(point_i[1], point_j[1]), 0)
                    num_point = 2
                else:
                    temp = (max(point_i[0], point_j[0]), min(point_i[0], point_j[0]), max(point_i[1], point_j[1]),
                            min(point_i[1], point_j[1]), abs(point_i[0] - point_j[0]) * abs(point_i[1] - point_j[1]))
                    num_point = 2

                for k in range(K):
                    if k == i or k == j:
                        continue
                    for point in array[k]:
                        if point[0] >= temp[1] and point[0] <= temp[0] and point[1] >= temp[3] and point[1] <= temp[2]:
                            num_point += 1
                            break

                if temp[4] < ans and num_point == K:
                    ans = temp[4]

print(ans)
