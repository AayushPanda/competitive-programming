def main():
    from sys import stdin, exit
    input = stdin.readline

    n, d, k, x = map(int, input().split())
    a = [int(input()) for _ in range(n)]
    p = int(input())

    for i in range(n):
        while a[i] >= p:
            a[i] = a[i] * ((100-x)//100)
            k -= 1

            if k == 0 and a[-1] >= p:
                print("NO")
                exit()

    print("YES")

main()