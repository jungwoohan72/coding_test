import sys

import sys

K, P, N = list(map(int, sys.stdin.readline().split()))

ans = K
for i in range(N*10):
        ans = ((ans % 1000000007)*(P % 1000000007)) % 1000000007

print(ans)