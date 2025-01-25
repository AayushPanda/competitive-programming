def main():
    import sys
    input = sys.stdin.readline

    m, n = map(int, input().split())
    safes = sorted([int(input()) for _ in range(n)])
    sums = [m]
    avs = [m]

    for x in range(1, n + 1):
        sums.append(sums[x-1]+safes[x-1])
        avs.append(sums[x]/(x+1))
    if sum(safes)/n == m:
        print(0)
    else:
        print(avs[::-1].index(min(avs)))
#    print(avs)


main()

# 50 4
# 50 - 50
# 10 - 30
# 100 - 53.33
# 150 - 77.5
# 280 - 118
