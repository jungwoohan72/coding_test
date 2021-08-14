import sys

n, m = list(map(int, sys.stdin.readline().split()))
array = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(array)

array = sorted(array, reverse = True)

while start <= end:
    total_sum = 0
    mid = (start+end)//2
    for num in array:
        if num > mid:
            total_sum += (num-mid)
        else:
            break

    if total_sum >= m:
        max_height = mid
        start = mid+1
    else:
        end = mid-1

print(max_height)