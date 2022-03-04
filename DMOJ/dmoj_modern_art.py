def main():
    import sys
    input = sys.stdin.readline

    m = int(input())
    n = int(input())
    k = int(input())

    r = [0] * m
    c = [0] * n

    for x in range(k):
        t, i = input().split()
        i = int(i) - 1

        if t == 'R':
            r[i] += 1
        else:
            c[i] += 1

    golds = 0

    for x in r:
        for y in c:
            if (x + y) % 2 != 0:
                golds += 1

    print(golds)


main()
