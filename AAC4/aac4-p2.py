import sys

def main():
    input = sys.stdin.readline

    n, q = map(int, input().split(' '))
    lights = map(int, input().split(' '))

    for x in range(q):
        t = int(input())
        remainders = list(map(lambda a: (t % a) == 0, lights))

        if False in remainders:
            print(remainders.index(False)+1)
        else:
            print(-1)

main()