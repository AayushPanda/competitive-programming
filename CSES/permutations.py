n = int(input())

if n == 1:
    print(n)
elif n <= 3:
    print("NO SOLUTION")
else:
    if n % 2 == 0:
        print( ' '.join(map(str, [x for x in range(1, n) if x % 2 != 0][::-1] + [x for x in range(1, n+1)[::-1] if x % 2 == 0])))
    else:
        print( ' '.join(map(str, [x for x in range(1, n+1) if x % 2 != 0][::-1] + [x for x in range(1, n)[::-1] if x % 2 == 0])))

