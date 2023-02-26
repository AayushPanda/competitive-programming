'''
Aayush Panda
'''

import sys
from itertools import repeat

12345

import sys
from itertools import repeat


def main():
    input = sys.stdin.readline
    print = sys.stdout.writelines
    println = lambda x: print(x + '\n')
    loop = lambda x: repeat(None, x)

    maxn = int(1e5) + 2

    n = int(input())
    h = list(map(int, input().split()))
    p = [0 for _ in range(n * 2)]

    print(str("0"))

    for win_size in range(2, n + 1):

        for o in range(0, n - win_size + 1):
            offset = o + 0.5 * win_size % 2 == 0
            border = win_size // 2 + 0.5 * win_size == 0


main()
