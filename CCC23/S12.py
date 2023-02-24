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

    #maxn = int(1e5) + 2

    c = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    p = 0

    for x in range(c):
        if x%2 == 0:
            if x==0:
                if a[x]:
                    p += 3*a[x] - a[x+1]
            elif x==c-1:
                if a[x]:
                    p += 3*a[x] - a[x-1]
            else:
                if a[x]:
                    p += 3*a[x] - a[x-1] - a[x+1]
        else:
            if x==c-1:
                if a[x]:
                    p += 3*a[x] - a[x-1]
            else:
                if a[x]:
                    p += 3*a[x] - a[x-1] - a[x+1]

    println(str(p))



main()