def selectPath(s, l, r):
    if s-l == s-r:
        return(r>l)
    else:
        return(abs(s-r) > abs(s-l))

def main():
    input()
    m = int(input())

main()