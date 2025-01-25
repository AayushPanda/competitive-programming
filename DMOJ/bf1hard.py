import sys


def main():
    input = sys.stdin.readline
    print = sys.stdout.writelines

    n = int(input())
    nums = []

    for x in range(n):
        nums.append(input())

    for n in sorted(nums):
        print(n)

main()
