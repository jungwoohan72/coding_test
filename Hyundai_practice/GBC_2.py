import sys

n,m = map(int, sys.stdin.readline().split())

given = []

for _ in range(n):
    length, limit = map(int, sys.stdin.readline().split())
    for _ in range(length):
        given.append(limit)

actual = []

for _ in range(m):
    length, limit = map(int, sys.stdin.readline().split())
    for _ in range(length):
        actual.append(limit)

check = []
for a in range(len(actual)):
    if actual[a] > given[a]:
        check.append(actual[a]-given[a])

ans = max(check) if check else 0
print(ans)
