import sys


def main():
    n = int(input())
    vals = []
    array = []

    for x in range(1, n):
        print('?', str(x), str(x+1))
        sys.stdout.flush()
        vals.append(int(input()))

    for x in range(n-2):
        array.append(- vals[x+1] + vals[x])

    print('? 1 2')
    sys.stdout.flush()

    if not array:
        second_elem = int(input()) // 2
    else:
        second_elem = (array[0]+int(input()))//2

    print(*['!', vals[0] + second_elem, second_elem] + array)



main()