a = input()

last = ''
best = 1
longest = 1
for c in a:
    if c == last:
        longest += 1
        best = max(longest, best)
    else:
        longest = 1
    last = c

print(best)