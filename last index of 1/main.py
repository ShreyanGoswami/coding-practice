# Given a string S consisting only '0's and '1's,  print the last index of the '1' present in it.
def lastIndexOfOne(s):
    i = len(s) - 1
    while(i >= 0):
        if s[i] == '1':
            return i + 1
        i = i -1
    return -1


def main():
    t = int(input())
    for i in range(0,t):
        inp = input().strip()
        if inp is not None and inp != '':
            count = lastIndexOfOne(inp)
            print(count)

main()