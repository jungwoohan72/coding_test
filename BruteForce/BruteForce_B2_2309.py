from collections import deque

list_ = []
deq = deque()

for i in range(9):
  _ = int(input())
  list_.append(_)
  deq.append(_)

keep = True

while keep:
  temp = list_[:]
  num = deq.pop()
  idx = temp.index(num)
  temp.pop(idx)

  for i in range(len(temp)):

    temp2 = temp[:]
    temp2.pop(i)

    if sum(temp2) == 100:
      ans = sorted(temp2)
      keep = False
      break

for i in ans:
  print(i)