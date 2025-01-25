def main():
    import sys
    input = sys.stdin.readline
    from math import ceil
    n = int(input())
    stones = list(map(int, input().split()))
    even = sum([ceil(stones[x] / 2) for x in range(n) if stones[x] % 2 == 0])
    odd = sum([ceil(stones[x] / 2) for x in range(n) if stones[x] % 2 != 0])

    if odd >= even:
        print('Alice')
    elif even > odd:
        print('Duke')


main()
