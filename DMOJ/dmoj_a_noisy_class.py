def main():
    input()
    m = int(input())

    output = 'Y'
    links = []
    for x in range(m):
        link = input()
        if link[::-1] not in links:
            links.append(link)
        else:
            output = 'N'

    print(output)

main()