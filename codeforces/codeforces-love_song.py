import sys

input = sys.stdin.readline


def main():
    n, q = map(int, input().split())
    s = input()

    counts = [0]
    idx = 0
    for char in s:
        counts.append((ord(char) - 96) + counts[idx])
        idx += 1

    qn = 0
    while qn < q:
        a, b = map(int, input().split())

        print(counts[b] - counts[a-1])

        qn += 1


main()
