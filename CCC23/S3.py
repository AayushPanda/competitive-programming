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

    n, m, r, c = map(int, input().split())

    println('a'*m)
    for i in range(n-1):
        println('a' + 'b'*(m-1))




main()