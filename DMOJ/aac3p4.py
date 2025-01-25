import sys


def main():
    input = sys.stdin.readline
    #print = sys.stdout.writelines

    n, m = [int(x) for x in input().split()]
    Bs = [int(x) for x in input().split()]
    As = [int(x) for x in input().split()]

    y = 0
    x = 0
    c = 0

    skipx = []

    while y < n:
        x = 0
        if Bs[y] == -1:
            y += 1
            continue
        while x < m:

            Bt = Bs[y]
            At = As[x]

            if At == -1:
                x += 1
                continue

            if Bt + x == At + y and x not in skipx:
                skipx.append(x)
                x = 0
                c += 1
                break

            x += 1
        y += 1

    print(c)



main()