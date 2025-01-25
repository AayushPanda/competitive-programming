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
    for x in a: p+=x

    println(str(3*p))


main()