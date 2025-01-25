for x in range(int(input())):
    ans = "".join([[str(x+2) for x in range(8) if char in 'ABC DEF GHI JKL MNO PQRS TUV WXYZ'.split()[x]][0] if char.isalpha() else char for char in input() if char != '-'])
    print(ans[:3] + '-' + ans[3:6] + '-' + ans[6:10])

# Normal code:
# divs = 'ABC DEF GHI JKL MNO PQRS TUV WXYZ'.split()
#
# for x in range(int(input())):
#     ans = ''
#     for char in input():
#         if char != '-':
#             if char.isalpha():
#                 for x in range(8):
#                     if char in divs[x]:
#                         ans += str(x+2)
#             else:
#                 ans += char
#     print(ans[:3] + '-' + ans[3:6] + '-' + ans[6:10])
