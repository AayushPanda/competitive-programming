def main():
    import sys
    input = sys.stdin.readline

    n, e = map(int, input().split())
    o = n - e
    op = ('12' * (o // 2) + '1' * e)

    if n != len(op):
        print(-1)
    else:
        print(' '.join(op))


main()