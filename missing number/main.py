# Given an array C of size N-1 and given that there are numbers from 1 to N with one element missing, the missing number is to be found.
def findMissing(arr):
    n = [0] * (len(arr) + 1)
    for x in arr:
        n[x-1] = 1
    for i in range(0,len(n)):
        if n[i] == 0:
            return i+1

def main():
    t = int(input())
    for i in range(0,t):
        n = int(input())
        inp = input().strip()
        if inp is not None and inp != '':
            inp = inp.split(' ')
            inp = [int(i) for i in inp]
            missingNumber = findMissing(inp)
            print(missingNumber)

main()