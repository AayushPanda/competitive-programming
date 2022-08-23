import sys


def main():
    #input = sys.stdin.readline
    #print = sys.stdout.writelines
    n=input()
    arr = list(set(list(map(int, input().split()))))
    print(len(arr) - arr.__contains__(0))

main()