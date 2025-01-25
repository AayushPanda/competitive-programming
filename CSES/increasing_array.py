l = int(input())
a = list(map(int, input().split()))
moves = 0

for x in range(1, l):
    moves += min(a[x] - a[x - 1], 0)
    a[x] = max(a[x], a[x-1])

print(0-moves)
