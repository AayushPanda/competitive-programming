from collections import Counter

counts = Counter(input())
currCounts = Counter(input())

shoppingCart = 0

for key in currCounts.keys():
    if key in counts.keys():
        counts[key] = counts[key] - currCounts[key]

        if counts[key] <= 0


        currCounts[key] = 0

for key in counts.keys():
    shoppingCart += counts[key]

if shoppingCart <= 0:
    shoppingCart = 0

print(shoppingCart)
