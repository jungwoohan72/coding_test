import sys

n, k = map(int, sys.stdin.readline().split())

idx = 0

while n != 1:
    if n % k == 0:
        n /= k
        idx += 1
    else:
        n -= 1
        idx += 1