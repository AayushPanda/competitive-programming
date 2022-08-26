a = [-1, 2, 4, -3, 5, 2, -5, 2]

sum = 0
best = 0

for x in range(len(a)):
    sum = max(a[x], sum + a[x])
    best = max(sum, best)

print(best)
