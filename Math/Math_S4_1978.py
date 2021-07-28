n = int(input())
arr = list(map(int, input().split()))

def Eratosthenes(array: list):
    max_ = max(array)
    arr = [x for x in range(2,max_+1)]

    num = 2

    while num != max_:
        for i in range(len(arr)):
            if arr[i] == num:
                continue
            if arr[i] % num == 0:
                arr[i] = 0
        num += 1

    arr = [y for y in arr if y != 0]

    return arr

count = 0
ans = Eratosthenes(arr)

for num in arr:
    if num == 1:
        continue
    if num in ans:
        count += 1

print(count)
