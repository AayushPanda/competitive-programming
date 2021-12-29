import sys

input = sys.stdin.readline


def main():
    x = int(input())
    y = int(input())

    x, y = min(x, y, 9), min(9, max(x, y))

    ans = max(0, x - abs(10 - y) + 1)

    if ans == 1:
        way = " way "
        are = " is "
    else:
        way = " ways "
        are = " are "

    print('There' + are + str(ans) + way + "to get the sum 10.")


main()
