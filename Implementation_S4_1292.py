n, m = list(map(int, input().split()))

flag = True
num = 1
arr = []
ans = 0
idx = 0

while flag:
    for i in range(num):
        arr.append(num)
        idx += 1
        if idx >= n and idx <= m:
            ans += arr[idx-1]
        if idx == m:
            flag = False
    num += 1

print(ans)