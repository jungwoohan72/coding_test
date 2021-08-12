import sys

n = int(sys.stdin.readline())

array = []
for _ in range(n):
    array.append(tuple(list(sys.stdin.readline().split())))

array = sorted(array, key = lambda student: student[1])

for student in array:
    print(student[0], end = ' ')