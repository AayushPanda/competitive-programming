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

    arr = []
    neg = 0
    pos = 0
    zero = 0
    for _ in loop(int(input())):
        x = int(input())
        if x < 0:
            neg += 1
        elif x > 0:
            pos += 1
        else:
            zero += 1
        arr.append(x)
    arr.sort()

    prod = arr[-1]
    arr[-1] = 1

    if neg % 2 == 0:
        for i in range(neg):
            prod *= arr[i]
    else:
        for i in range(neg-1):
            prod *= arr[i]
    if pos > 0:
        for i in range(neg+zero, neg+zero+pos):
            prod *= arr[i]

    println(str(prod))

main()
