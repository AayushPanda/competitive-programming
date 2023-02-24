'''
Aayush Panda
'''

import sys
#from itertools import repeat

def main():
    #input = sys.stdin.readline
    print = sys.stdout.writelines
    println = lambda x: print(x + '\n')
    #loop = lambda x: repeat(None, x)

    #maxn = int(1e5) + 26

    c = int(input())
    a = [0] + [int(x) for x in input().split()] + [0]
    b = [0] + [int(x) for x in input().split()] + [0]

    p = 0

    for x in range(1, c+1):
        if x%2 != 0:
                if a[x]:
                    p += 3*a[x] - a[x-1] - a[x+1] - b[x]
                if b[x]:
                    p += 3*b[x] - b[x-1] - b[x+1] - a[x]
        else:
                if a[x]:
                    p += 3*a[x] - a[x-1] - a[x+1]
                if b[x]:
                    p += 3*b[x] - b[x-1] - b[x+1]

    println(str(p) + ' ')



main()