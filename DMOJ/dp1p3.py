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

    #Longest increasing subsequence
    arr = [int(input()) for _ in range(int(input()))]
    n = len(arr)
    lis = [1]*n
    for i in range (1 , n):
        for j in range(0 , i):
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 :
                lis[i] = lis[j]+1
    maximum = 0
    for i in range(n):
        maximum = max(maximum , lis[i])
    print(str(maximum))


main()
