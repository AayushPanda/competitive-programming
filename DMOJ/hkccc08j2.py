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

    for _ in loop(int(input())):
        s = list(input)



main()