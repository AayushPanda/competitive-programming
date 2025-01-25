def main():
    from collections import Counter
    import sys
    input = sys.stdin.readline
    print = sys.stdout.writelines

    letters = []
    for x in range(int(input())):
        letters.append(input()[:-1])

    for letter in letters:
        ans = "YES"
        
        for y in range(len(letter) - 1):
            y += 1
            
            for x in range(len(letter) - y):
                ss = letter[x:x + y + 1]
                c = list(Counter(ss).values())

                for char in set(letter):
                    if char not in set(letter[x:x + y + 1]):
                        c.append(0)
                        if max(c) > 1:
                            ans = "NO"
                        break

                if ans=="NO":
                    break

                nmin, nmax = c[0], c[0]

                for idx in range(len(c)):
                    if c[idx] < nmin: nmin = c[idx]
                    if c[idx] > nmax: nmax = c[idx]

                dmax = nmax - nmin

                if dmax > 1:
                    ans = "NO"
                    break
            if ans == "NO":
                break

        print(ans + '\n')


main()
