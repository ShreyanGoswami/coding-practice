# Given an array of positive integers. The task is to find inversion count of array.

# Inversion Count : For an array, inversion count indicates how far (or close) the array is from being sorted. If array is already sorted then inversion count is 0. If array is sorted in reverse order that inversion count is the maximum.
# Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.


def invesionCountNaive(arr):
    count = 0
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                count = count + 1
    return count


def mergeTwoSortedArrays(arr, temp, start, end):
    # Start to mid is first array
    # Mid + 1 to end is second array
    mid = (start + end) >> 1

    leftStart = start
    leftEnd = mid
    rightStart = leftEnd + 1
    rightEnd = end
    index = leftStart

    invCount = 0

    while leftStart <= leftEnd and rightStart <= end and rightStart < len(arr):
        if arr[leftStart] <= arr[rightStart]:
            temp[index] = arr[leftStart]
            leftStart += 1
        else:
            temp[index] = arr[rightStart]
            rightStart += 1
            invCount += mid - leftStart + 1
        index += 1

    while leftStart <= leftEnd:
        temp[index] = arr[leftStart]
        leftStart += 1
        index += 1

    while rightStart <= end and rightStart < len(arr):
        temp[index] = arr[rightStart]
        rightStart += 1
        index += 1

    arr[start:rightStart] = temp[start:index]
    return invCount


def mergeSort(arr, temp, start, end):
    if start == end:
        return 0
    mid = (start + end) >> 1

    invCount = 0
    invCount += mergeSort(arr, temp, start, mid)
    invCount += mergeSort(arr, temp, mid + 1, end)

    invCount += mergeTwoSortedArrays(arr, temp, start, end)
    return invCount


def invesionCount(arr):
    start = 0
    end = len(arr)
    temp = [0] * len(arr)  # TODO remove this array
    return mergeSort(arr, temp, start, end)


def main():
    t = int(input())
    for i in range(0, t):
        n = int(input())
        inp = input().strip()
        if inp is not None and inp != "":
            inp = inp.split(" ")
            inp = [int(i) for i in inp]
            count = invesionCount(inp)
            print(count)


main()
