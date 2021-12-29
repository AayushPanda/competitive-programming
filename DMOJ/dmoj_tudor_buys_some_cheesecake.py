from collections import Counter

counts = Counter(input())
currCounts = Counter(input())

counts.subtract(currCounts)
ndelta = 0

for key in counts.keys():
    ndelta += max(0, counts[key])

print(ndelta)
