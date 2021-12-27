def sendToBack(arr):
    arr.append(arr[0])
    del (arr[0])
    return arr


def main():
    length, zeros = map(int, input().split(' '))
    string = input()
    chars = []

    cheers = input().split(' ')

    nzero = 0

    for char in string:
        if char == "0":
            chars.append(int(cheers[nzero]))
            nzero += 1
        else:
            chars.append(char)

    while zeros > 0:
        if type(chars[0]) == int:
            if chars[0] == 0:
                del (chars[0])
                zeros -= 1
            else:
                chars[0] = chars[0] - 1
                if chars[0] == 0:
                    del (chars[0])
                    zeros -= 1
                else:
                    chars = sendToBack(chars)
        else:
            intindex = [type(a) == int for a in chars].index(True)
            chars = chars[intindex:] + chars[0:intindex]

    print("".join(chars))


main()
