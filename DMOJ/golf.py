def main():
    import sys
    input = sys.stdin.readline
    # coin change much?

    dist = int(input())
    nclubs = int(input())
    clubs = [int(input()) for _ in range(nclubs)]
    minimum = [0] + [420 for _ in range(dist)]

    for d in range(dist + 1):
        for c in clubs:
            if d + c <= dist:
                if minimum[d] + 1 < minimum[d + c]:
                    minimum[d + c] = minimum[d] + 1

    if minimum[dist] < 420:
        print(f"Roberta wins in {minimum[dist]} strokes.")
    else:
        print("Roberta acknowledges defeat.")


main()
