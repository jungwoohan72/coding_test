import sys

n = int(input())
cand = list(map(int, sys.stdin.readline().split()))
m = int(input())
target = list(map(int, sys.stdin.readline().split()))

# # Using 'in'
# for tar in target:
#     if tar in cand:
#         print('yes', end = ' ')
#     else:
#         print('no', end = ' ')

# Using binary search
# O(NlogN) for sorting the candidate list
# O(MlogN) for finding targets

def binary_search(array, target, start, end):
    if start > end:
        return 'no'
    mid = (start+end)//2
    if array[mid] == target:
        return 'yes'
    elif target < array[mid]:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

cand.sort()
for tar in target:
    print(binary_search(cand, tar, 0, n-1), end = ' ')
