# Generate primes 

def genfibs(n):
    if n == 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    a = 1
    b = 1
    c = 2
    fibs = [1, 1]
    for i in range(3, n+1):
        c = a + b
        a = b
        b = c
        fibs.append(c)
    return fibs



print(genfibs(10))
print([sum(genfibs(i)) for i in range(1, 10)])