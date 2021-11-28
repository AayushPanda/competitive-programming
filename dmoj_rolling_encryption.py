from collections import Counter
import sys

input = sys.stdin.readline
chars = list('abcdefghijklmnopqrstuvwxyz')

winsize = int(input())
winidx = 0
string = list(str(input()))[0:-1]

def maxDict(dict):
    return max(dict, key=lambda key: dict[key])

for x in range(len(string)-winsize):
    window = string[x:x+winsize]
    wincount = Counter(window)
    maxcount = maxDict(wincount)
    string[x+winsize] = chars[chars.index(maxcount) + chars.index(string[x+winsize])]

print("".join(string))

