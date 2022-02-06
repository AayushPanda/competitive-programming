from collections import Counter
s = "carrace"
s = all([x%2==0 for x in Counter(s).values()])
print(s)