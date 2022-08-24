'''
Aayush Panda
'''

import sys


def caesar(m, shift, l):
    if l:
        return ''.join([chr((ord(c) - ord('a') + shift) % 26 + ord('a')) for c in m])
    else:
        return ''.join([chr((ord(c) - ord('a') - shift) % 26 + ord('a')) for c in m])


def main():
    input = sys.stdin.readline
    print = sys.stdout.writelines
    println = lambda x: print(str(x) + '\n')

    code = input().strip()
    m = input().strip()
    shift = 0

    while shift < 26:
        sd = caesar(m, shift, 1)
        if sd in code:
            println(shift)
            println(caesar(code, shift, 0))
            break
        shift += 1


main()
