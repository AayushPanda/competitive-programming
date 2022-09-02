n = int(input())
out = str(n)
while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n = (n*3)+1
    out += ' ' + str(n)

print(out)