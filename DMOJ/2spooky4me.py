'''
Aayush Panda
'''

import sys
from itertools import repeat

def sortXbyY(X,Y):
    return [(y,x) for y,x in sorted(zip(Y,X))]

def main():
    input = sys.stdin.readline
    print = sys.stdout.writelines
    println = lambda x: print(x + '\n')
    loop = lambda x: repeat(None, x)

    maxn = int(1e5) + 2
    N,L,S = map(int, input().split())

    houses = [(L+1, 0)]
    for _ in loop(N):
        a,b,s = map(int, input().split())
        houses.append((a,s))
        houses.append((b+1,-s))
    houses.sort()

    spook = 0
    for i in range(len(houses)-1):
        spook += houses[i][1]
        if spook >= S:
            L -= houses[i+1][0] - houses[i][0]

    println(str(L))

main()