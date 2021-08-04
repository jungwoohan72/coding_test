import sys

n, m, k = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()

first = num_list[-1]
second = num_list[-2]

ans = 0
idx = 1

for _ in range(m):
    if idx % k != 0:
        idx += 1
        ans += first
    else:
        idx += 1
        ans += second

print(ans)