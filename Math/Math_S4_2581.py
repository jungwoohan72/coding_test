def Eratosthenes(lower: int, upper: int):
    arr = [x for x in range(2, upper+1)]

    num = 2

    while num < upper**0.5:
        for i in range(len(arr)):
            if arr[i] == num:
                continue
            if arr[i] % num == 0:
                arr[i] = 0
        num += 1

    arr = [y for y in arr if y != 0 and y >= lower]

    return arr

lower = int(input())
upper = int(input())

arr = Eratosthenes(lower, upper)

if arr:
    print(sum(arr))
    print(arr[0])
else:
    print(-1)