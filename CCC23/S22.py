'''
Aayush Panda
'''

import sys
#from itertools import repeat

def main():
#    input = sys.stdin.readline
    print = sys.stdout.writelines
    println = lambda x: print(x + '\n')
#    loop = lambda x: repeat(None, x)

    n = int(input())
    h = list(map(int, input().split()))

    print('0 ')

    for i in range(2, n+1):     #Length
        min_assym = -1
        for j in range(n-i+1):    #Offset
            win = h[j:j+i]

            m = []

            if i % 2 == 0:
                a = win[:i//2]
                b = win[i//2:]
            else:
                a = win[:i//2]
                m = [win[i//2]]
                b = win[(i//2)+1:]
            b = b[::-1]

            #println(str(a+m+b[::-1]))

            assym = 0

            if j==0:
                for k in range(i//2):
                    assym += abs(a[k] - b[k])
                min_assym = assym
            else:
                for k in range(i//2):
                    assym += abs(a[k] - b[k])
                    if assym>=min_assym: break
                
                if assym < min_assym:
                    min_assym = assym
                
        print(str(min_assym) + ' ')
main()