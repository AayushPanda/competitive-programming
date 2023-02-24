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

    maxn = int(1e5) + 2

    n = int(input())
    h = list(map(int, input().split()))

    print(str("0 "))

    for i in range(2, n+1):
        assym_min = maxn
        for j in range(n-i+1):
            a  = h[j:i+j]
            b = a[i//2:]
            a = a[:i//2]

            m = 'm'

            if i %2!=0: 
                m = b[0]
                b = b[1:]
            b = b[::-1]
            
            assym = 0

            for k in range(i//2):
                assym += abs(a[k] - b[k])
                if assym > assym_min:
                    break
            
            if assym < assym_min:
                assym_min = assym
    
        print(str(assym_min) + ' ')
            
main()