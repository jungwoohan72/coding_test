import sys
from collections import deque

n = int(sys.stdin.readline())

array = deque()
for _ in range(n-1):
    a, b, ab, ba = list(map(int, sys.stdin.readline().split()))
    array.append((a,b,ab,ba))

an, bn = list(map(int, sys.stdin.readline().split()))
array.append((ab,bn))

ans = 0
while array:
    a,b,ab,ba = array.popleft()
    if a < b:
        ans = 