T = int(input())


def binary(n):
    ans = []

    while n > 0:
        if n == 1:
            ans.append(0)
            n -= 1
            break

        temp = 0
        val = n
        while val > 1:
            val = val // 2
            temp += 1

        ans.append(temp)
        n -= 2 ** temp

    return reversed(ans)


for i in range(T):
    print(" ".join(str(x) for x in binary(int(input()))))