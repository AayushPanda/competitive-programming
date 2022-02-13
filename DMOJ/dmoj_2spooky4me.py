def main():
    import sys
    input = sys.stdin.readline

    NLS = list(map(int, input().split()))
    sectors = []

    for x in range(NLS[0]):
        sectors.append(list(map(int, input().split())))

    locations = []

    for x in range(1,NLS[1]):
        locations.append(0)
        for sector in sectors:
            if sector[0] <= x <= sector[1]:
                locations[x-1] += sector[2]

    print(sum([x<NLS[2] for x in locations]))
main()



look at gaps between the rght most and the left msot for the boundaries of the decorations
    