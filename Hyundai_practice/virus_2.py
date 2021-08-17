import sys

K, P, N = list(map(int, sys.stdin.readline().split()))

# def virus(k, p, n):
#         if n == 0:
#                 return k
#         else:
#                 return p*virus(k, p, n-1)

# ans = virus(K, P, N) % 1000000007

ans = K
for i in range(N):
        ans = ((ans % 1000000007)*(P % 1000000007)) % 1000000007

print(ans)