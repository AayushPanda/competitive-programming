import sys
from itertools import repeat


def main():
    input = sys.stdin.readline
    print = sys.stdout.writelines
    println = lambda x: print(str(x) + '\n')
    loop = lambda x: repeat(None, x)

    n, m = map(int, input().split())
    a = [0.0] * n
    pie = 1

    for _ in loop(m):
        n, p = map(float, input().split())
        p /= 100
        n -= 1

        a[n] += pie * p
        pie = pie * (1-p)

    for x in a:
        println(x)


main()
