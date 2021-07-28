history = []

for i in range(10):
  history.append(list(map(int, input().split())))

curr = 0
ans = 0

for out_, in_ in history:
  curr -= out_
  curr += in_
  if ans < curr:
    ans = curr

print(ans)