# Given an array A of N positive numbers. The task is to find the position where equilibrium first occurs in the array. 
# Equilibrium position in an array is a position such that the sum of elements before it is equal to the sum of elements after it.

def findEquilibrium(arr):
    if len(arr) == 1:
        return 1
    if len(arr) == 2:
        return -1
    lhsSum = arr[0]
    pivot = 1
    rhsSum = 0
    for i in range(2, len(arr)):
            rhsSum = rhsSum + arr[i]
    
    while True:
        if lhsSum == rhsSum:
            return pivot + 1
        else:
            if pivot == len(arr) - 1:
                return -1
            lhsSum = lhsSum + arr[pivot]
            rhsSum = rhsSum - arr[pivot+1]
            pivot = pivot + 1


def main():
    t = int(input())
    for i in range(0,t):
        n = int(input())
        inp = input().strip()
        if inp is not None and inp != '':
            inp = inp.split(' ')
            inp = [int(i) for i in inp]
            pos = findEquilibrium(inp)
            print(pos)

main()