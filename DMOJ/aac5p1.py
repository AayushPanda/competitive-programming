import sys

input = sys.stdin.readline

n = int(input())

a = map(int, input().split())
nOdd = sum([x & 1 == 0 for x in a])
nEven = n - nOdd

oddPairs = (nOdd - (nOdd % 2)) // 2
evenPairs = (nEven - (nEven % 2)) // 2

print(oddPairs + evenPairs)
