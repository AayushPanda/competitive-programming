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
    h = list(map(int, input().split()))

    print(str("0 "))

    for win_size in range(2, n+1):
        min_assym = -1
        first = True
        for offset in range(0, n-win_size+1):
            win = h[offset:offset+win_size]
            left = win[:win_size//2]
            right = win[win_size//2:]
            if win_size % 2 != 0:
                right = right[1:]
            right = right[::-1]

            assym = 0

            if first:
                for i in range(win_size//2):
                    assym += abs(left[i] - right[i])
                min_assym = assym
                first = False
            else:
                for i in range(win_size//2):
                    assym += abs(left[i] - right[i])
                    if assym>=min_assym: break
                if assym<=min_assym:
                    min_assym = assym
        
        print(str(min_assym) + ' ')


main()