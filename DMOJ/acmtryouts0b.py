import sys


def main():
    input = sys.stdin.readline

    for _ in range(int(input())):
        n = int(input())
        a = input()
        b = input()
        print("".join(a[x] + b[x] for x in range(n))[::-1])


main()
