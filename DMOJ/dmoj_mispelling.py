for i in range(1, int(input()) + 1):
    d = input()
    si = d.index(' ')
    n = int(d[:si])
    s = d[si+1:]

    print(str(i) + ' ' + s[:n-1] + s[n:])
