a = list(input())

chess = [[i for i in range(8)] for _ in range(8)]

hor = [-2,-2,-1,-1,2,2,1,1]
ver = [-1,1,-2,2,-1,1,-2,2]

ans = 0
column_idx = int(ord(a[0])) - int(ord('a')) # 0부터 시작
row_idx = int(a[1]) # 1부터 시작

for i in range(len(hor)):
    if row_idx+ver[i] < 1 or row_idx+ver[i] > 8 or column_idx+hor[i] < 0 or column_idx+hora[i] > 7:
        continue
    else:
        ans += 1

print(ans)