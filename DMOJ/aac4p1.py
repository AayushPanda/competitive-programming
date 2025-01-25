# import sys
#
#
# def main():
#     input = sys.stdin.readline
#     print = sys.stdout.writelines
#
#     length, zeros = map(int, input().split())
#     string = input()[:-1]
#     cheers = list(map(int, input().split()))
#
#     maxCheerZeroIdx = [i for i, x in enumerate(string) if x == "0"][(zeros - 1) - cheers[::-1].index(max(cheers))]
#
#     print([x for x in string[maxCheerZeroIdx:] + string[:maxCheerZeroIdx] if x != '0'])
#     print('\n')
#
#
# main()

l, z = map(int, input().split())

s = input()

c = list(map(int, input().split()))

zl = []

for i, e in enumerate(s):
    if e == '0': zl.append(i)

r = max(c)

idx = z - c[::-1].index(r) - 1

ans = s[zl[idx]:] + s[:zl[idx]]

print(ans.replace('0', ''))
