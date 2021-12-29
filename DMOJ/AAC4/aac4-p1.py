import sys


def main():
    input = sys.stdin.readline
    print = sys.stdout.writelines

    length, zeros = map(int, input().split())
    string = input()[:-1]
    cheers = list(map(int, input().split()))

    maxCheerZeroIdx = [i for i, x in enumerate(string) if x == "0"][(zeros - 1) - cheers[::-1].index(max(cheers))]

    print([x for x in string[maxCheerZeroIdx:] + string[:maxCheerZeroIdx] if x != '0'])
    print('\n')


main()
