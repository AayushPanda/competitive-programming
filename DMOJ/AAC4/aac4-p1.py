import sys


def main():
    input = sys.stdin.readline
    print = sys.stdout.writelines

    length, zeros = map(int, input().split())  # Unused data
    string = input()[:-1]
    cheers = input().split()

    maxCheerZeroIdx = length - [i for i, x in enumerate(string[::-1]) if x == '0'][cheers[::-1].index(max(cheers[::-1]))]

    print([x for x in string[maxCheerZeroIdx:] + string[:maxCheerZeroIdx] if x != '0'])
    print('\n')


main()
s = str.split