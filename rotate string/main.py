# Given two strings a and b. The task is to find if a string 'a' can be obtained by rotating another string 'b' by 2 places.


def shiftLeft(s, n):
    return s[n:] + s[:n]


def shiftRight(s, n):
    return s[-n:] + s[:-n]


def main():
    t = int(input())
    for i in range(0, t):
        s = input()
        ans = input()
        sAfterShiftLeft = shiftLeft(s, 2)
        sAfterShiftRight = shiftRight(s, 2)
        if sAfterShiftLeft == ans:
            print(1)
        elif sAfterShiftRight == ans:
            print(1)
        else:
            print(0)


main()
