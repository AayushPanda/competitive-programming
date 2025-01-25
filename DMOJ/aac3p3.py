import sys


def main():
    input = sys.stdin.readline
    # print = sys.stdout.writelines

    n = int(input())
    n2 = n // 2
    a = sorted([int(x) for x in input().split()])

    l = a[:n2]
    h = a[n2:]

    if n % 2 != 0:
        sh = h[0]
        del h[0]

    a = []
    for i in range(n2):
        a += [l[i], h[i]]

    if n % 2 != 0:
        a.append(sh)

    print(" ".join(list(map(str, a))))
    bs = (''.join(["BS" for _ in range(n2)]))

    if n % 2 != 0:
        bs += 'E'

    print(bs)


main()
