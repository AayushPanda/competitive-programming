import sys

input = sys.stdin.readline

def query(a,b):
    print(f"? {a} {b}")
    return int(input())

def main():
    n = int(input())

    products = [query(1, x+1) for x in range(1, n)]

    if max(products) == n:
        a1 = 1
    else:
        a1 = min(products)

    print(f"! {a1}", end="")
    [print(" " + str(x//a1), end="") for x in products]
    print("\n")

main()
