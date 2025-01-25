'''
Aayush Panda
'''

import sys
from itertools import repeat

def main():
    input = sys.stdin.readline
    print = sys.stdout.writelines
    println = lambda x: print(x + '\n')
    loop = lambda x: repeat(None, x)

    maxn = int(1e5) + 2

    n = int(input())
    arr = []
    for _ in loop(n):
        arr.append(list(map(int, input().split())))

    for y in [i for i in range(n-1)][::-1]:
        for x in range(y+1):
            arr[y][x] += max(arr[y+1][x], arr[y+1][x + 1])

    print(str(arr[0][0]))

main()