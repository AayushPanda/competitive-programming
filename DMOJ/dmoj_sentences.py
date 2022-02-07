def main():
    import sys
    input = sys.stdin.readline
    n = int(input())
    for x in range(n):
        counts = [int(input()) for x in range(3)]
        subjects = [input()[:-1] for x in range(counts[0])]
        verbs = [input()[:-1] for x in range(counts[1])]
        objects = [input()[:-1] for x in range(counts[2])]

        for subject in subjects:
            for verb in verbs:
                for sobject in objects:
                    print(subject + ' ' + verb + ' ' + sobject + '.')
main()
