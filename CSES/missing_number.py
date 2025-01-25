l = int(input())
a = map(int, input().split())

print(int(l/2*(1 + l) - sum(a)))