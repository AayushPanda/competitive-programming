def main():
    for _ in range(int(input())):
        n, b = map(int, input().split())
        marks = list(map(int, input().split()))

        c = 0

        if sorted(marks) == marks:
            if c > b:
                print('No')
            else:
                print('Yes')
            continue

        c = 1

        v = [[marks[i], i] for i in range(n)]

        v = sorted(v, key=lambda i: i[0])

        for i in range(1, n):
            if v[i][0] != v[i - 1][1]:
                c += 1

        if c > b:
            print('No')
        else:
            print('Yes')


main()
