import sys

N = int(sys.stdin.readline())

current = 2
side = 2

for i in range(N):
        side += current-1
        current = side

print(side*side)