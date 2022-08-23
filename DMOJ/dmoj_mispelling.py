for i in range(1, int(input()) + 1):
    d = input()
    n = int(d[0])
    s = d[2:]
    print(str(i) + ' ' + s[:n-1] + s[n:])