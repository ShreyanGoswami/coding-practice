def arrangeArrayAlternatively(arr, n):
    if len(arr) == 1:
        return arr
    high = n - 1
    low = 0
    res = []
    while low < high:
        res.append(arr[high])
        res.append(arr[low])
        low += 1
        high -= 1
        if low == high:
            res.append(arr[high])
            break
    return res


def arrangeArrayAlternativelyOptimized(arr, n):
    if len(arr) == 1:
        return arr
    high = n - 1
    low = 0
    nextHigh, nextLow = 0, 0
    highPos = 0
    lowPos = 1
    while low < high:
        nextHigh = arr[high - 1]
        nextLow = arr[low + 1]  # TODO check if they are equal
        arr[lowPos] = arr[low]
        arr[highPos] = arr[high]
        low += 2
        high -= 1
        lowPos += 2
        highPos += 2
    return arr


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input().split()
        res = arrangeArrayAlternativelyOptimized(arr, n)
        print(" ".join(str(x) for x in res))
