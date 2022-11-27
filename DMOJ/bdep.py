"""
Aayush Panda
"""

import sys
from itertools import repeat

def main():
    input = sys.stdin.readline
    print = sys.stdout.writelines
    println = lambda x: print(x + '\n')
    loop = lambda x: repeat(None, x)

    p, y, t = map(int, input().split())

    def check():
        amount_after = 0
        for i in range(y):
            amount_after += mid
            amount_after += (amount_after * p) // 100
            if amount_after >= t: return True
        return False


    low, high = 1, t
    while low <= high:
        mid = (low + high) // 2
        if check(): ans, high = mid, mid-1
        else:
            low = mid + 1

    print(str(ans))


main()