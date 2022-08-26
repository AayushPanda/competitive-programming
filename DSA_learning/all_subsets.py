a = [x for x in range(10)]

# using bit representation of integers
b = ""
for _ in range(len(a)):
    b += '1'

n = int(b, 2)

for x in range(n):
    bitrep = f'{x:b}'
    bitrep = '0' * (len(a) - len(bitrep)) + bitrep
    subset = []

    for i in range(len(bitrep)):
        if bitrep[i] == '1':
            subset += a[i]

    print(subset)
