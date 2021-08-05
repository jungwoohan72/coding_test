n = int(input())

m = 60
s = 60

ans = 0
for i in range(n+15):
    for j in range(m):
        for k in range(s):
            temp = list((str(i)+str(j)+str(k)))

            if '3' in temp:
                ans += 1

print(ans)