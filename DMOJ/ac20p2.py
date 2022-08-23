import sys
from math import ceil
from itertools import repeat

def main():
    input = sys.stdin.readline
    print = sys.stdout.writelines

    n, q = map(int, input().split())

    a = [0] * (int(1e5) + 2)
    for i in input().split():
        a[int(i)] += 1

    for _ in repeat(None, q):
        t, n = map(int, input().split())

        if t == 1:
            c = a[n]
            a[n] = 0

            for s in [ceil(n/2), n//2]:
                a[s] += c

        else:
            print(str(a[n]) + '\n')

main()