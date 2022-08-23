n, k = map(int, input().split())
full = []
discounted = []
deltas = []

for x in range(n):
    a, b = map(int, input().split())
    full.append(a)
    discounted.append(b)
    deltas.append(a-b)

deltas, full, discounted = zip(*sorted(zip(deltas, full, discounted))[::-1])

cost = sum(discounted[:k]) + sum(full[k:])

print(cost)

# First problem of 2022!!
