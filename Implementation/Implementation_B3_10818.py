n = int(input())
num_list = map(int,input().split())

num_min = 1000000
num_max = -1000000

for num in num_list:
  if num < num_min:
    num_min = num
  if num > num_max:
    num_max = num

print(num_min, end=" ")
print(num_max)