import sys
input = sys.stdin.readline

t = int(input())

for x in range(t):
    a, b = map(int, input().split(' '))

    y = 0
    z = min(a, b) + 1

    while (z - y > 1):
        mean = (y + z) // 2
        a2 = a - mean
        b2 = b - mean

        if (a2 + b2 >= mean * 2):
            y = mean
        else:
            z = mean

    print(y)