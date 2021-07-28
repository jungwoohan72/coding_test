def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    remainder = array[1:]

    left = [x for x in remainder if x <= pivot]
    right = [y for y in remainder if y >= pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

n = int(input())

list_ = []

for i in range(n):
    list_.append(list(map(int, input().split())))

for x in list_:
    print(quick_sort(x)[-3])
