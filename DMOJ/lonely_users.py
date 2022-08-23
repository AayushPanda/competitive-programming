for _ in range(int(input())):
    n = int(input())

    if n == 2:
        print(n)
    else:
        print(max(0, n-1))