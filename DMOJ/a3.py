import sys
from itertools import repeat

def main():
    input = sys.stdin.readline
    print = sys.stdout.writelines
    println = lambda x: print(x + '\n')
    loop = lambda x: repeat(None, x)

    #maxn = int(1e5) + 2

    for _ in loop(int(input())):
        n = ((int(input())-192)//250) + 1
        println(str(192 + (n*250)))


main()