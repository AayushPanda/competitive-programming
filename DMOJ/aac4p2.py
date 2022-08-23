import math
import sys

input = sys.stdin.readline


def main():
    input = sys.stdin.readline

    n, q = map(int, input().split(' '))
    lights = list(map(int, input().split(' ')))

    plcm = [lights[0]]

    for x in range(1, n):
        lcm = math.lcm(plcm[x - 1], lights[x])

        if lcm >= 10 ** 9:
            break

        plcm.append(lcm)

    for i in range(q):
        t = int(input())

        l, r = 0, n - 1

        while l < r:
            mid = (l + r) // 2

            if t % plcm[mid] == 0:
                l = mid + 1
            else:
                r = mid
        if t % plcm[l] == 0:
            l += 1

        if l >= n:
            print(-1)
        else:
            print(l)


main()
