# Given a sorted and rotated array A of N distinct elements which is rotated at some point, and given an element K.
# The task is to find the index of the given element K in the array A.
# 3
# 9
# 5 6 7 8 9 10 1 2 3


def findRotationCount(arr, start, end):
    i = start
    j = end - 1
    while i < j:
        mid = (i + j) >> 1
        if arr[mid] > arr[mid + 1]:
            return mid + 1
        elif arr[mid] < arr[mid - 1]:
            return mid
        elif arr[mid] > arr[j]:
            i = mid + 1
        else:
            j = mid - 1
    if i == j:
        return i


def binarySearch(arr, k, start, end):
    i = start
    j = end - 1
    while i <= j:
        mid = (i + j) >> 1
        if arr[mid] == k:
            return mid
        if arr[mid] > k:
            j = mid - 1
        else:
            i = mid + 1
    return -1


def findK(arr, k):
    p = findRotationCount(arr, 0, len(arr))
    posLeft = binarySearch(arr, k, 0, p + 1)
    posRight = binarySearch(arr, k, p, len(arr))
    if posLeft != -1:
        return posLeft
    return posRight


def main():
    t = int(input())
    for i in range(0, t):
        n = int(input())
        inp = input().strip()
        k = int(input())
        if inp is not None and inp != "":
            inp = inp.split(" ")
            inp = [int(i) for i in inp]
            pos = findK(inp, k)
            print(pos)


main()
