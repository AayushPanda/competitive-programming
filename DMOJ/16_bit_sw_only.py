for _ in range(int(input())):
    a, b, c = [int(x) for x in input().split()]
    print(["16 BIT S/W ONLY", "POSSIBLE DOUBLE SIGMA"][a * b == c])
