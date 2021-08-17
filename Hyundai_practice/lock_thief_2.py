import sys
import heapq

w, n = list(map(int, sys.stdin.readline().split()))

q = []

for _ in range(n):
    weight, value = list(map(int, sys.stdin.readline().split()))
    heapq.heappush(q, (-value, weight)) # O(NlogN)

money = 0
while q:
    value, weight = heapq.heappop(q) # O(NlogN)
    if w - weight < 0:
        money += w*(-value)
        break
    else:
        money += weight*(-value)
        w -= weight

# Total O(2NlogN) -> O(NlogN)
# 1 <= N <= 10^6 -> O(NlogN) 가능

print(money)


######################### 시간제한 걸린다 ㅠ #########################
# import sys
# import time
#
# start = time.time()
#
# w, n = list(map(int, sys.stdin.readline().split()))
#
# array = []
#
# for _ in range(n):
#     array.append(tuple(map(int, sys.stdin.readline().split())))
#
# array = sorted(array, key = lambda x: x[1], reverse = True) # O(NlogN)
#
# money = 0
# for weight, value in array: # O(N)
#     if w - weight < 0:
#         money += w*value
#         break
#     else:
#         money += weight*value
#         w -= weight
#
# print(money)
# print(time.time()-start)
