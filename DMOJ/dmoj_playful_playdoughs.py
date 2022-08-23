import sys
from collections import Counter

def main():
    input = sys.stdin.readline
    #print = sys.stdout.writelines

    n, q = [int(x) for x in input().split()]

    a = dict(Counter([float(x) for x in input().split()]))

    for _ in range(q):
        t, n = [int(x) for x in input().split()]
        n = float(n)

        if t == 1:
            s = n/2
            q = a[n] * 2
            del a[n]

            try:
                a[s] += q
            except:
                a[s] = q

        else:
            print(a[n])

main()