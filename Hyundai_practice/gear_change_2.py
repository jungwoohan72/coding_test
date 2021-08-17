import sys

a = list(map(int, sys.stdin.readline().split()))

asc_ref = [i for i in range(1,9)]
dec_ref = list(reversed(asc_ref))

if a == asc_ref:
        print("ascending")
elif a == dec_ref:
        print("descending")
else:
        print("mixed")