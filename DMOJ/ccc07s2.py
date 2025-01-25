import sys


def main():
    input = sys.stdin.readline
    #print = sys.stdout.writelines

    n = int(input())

    boxes = []

    for _ in range(n):
        boxes.append(sorted(list(map(int, input().split()))))

    for _ in range(int(input())):
        boxa = sorted(list(map(int, input().split())))
        m = False
        for boxb in boxes:
            if all(a <= b for a, b in zip(boxa, boxb)):
                m = True
                print(str(boxb[0] * boxb[1] * boxb[2]))
                break
        if not m:
            print("Item does not fit.")


main()
