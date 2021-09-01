# Given an array A of size N having distinct elements,
# the task is to find the next greater element for each element of the array in order of their appearance in the array.
# If no such element exists, output -1


def nextLargestOptimized(arr, n):
    res = []
    s = []
    arr = arr[::-1]
    for x in arr:
        foundLargest = False
        while len(s) != 0 and s[-1] < x:
            s.pop()
        if len(s) == 0:
            res.append(-1)
        else:
            res.append(s[-1])
        s.append(x)
    return res[::-1]


def nextLargest(arr, n):
    res = []
    for i in range(n):
        isFound = False
        for j in range(i + 1, n):
            if arr[i] < arr[j]:
                isFound = True
                res.append(arr[j])
                break
        if isFound == False:
            res.append(-1)
    return res


if __name__ == "__main__":
    inp = input
    itos = int
    stoi = str
    t = itos(inp())
    for i in range(t):
        n = itos(inp())
        arr = list(map(itos, inp().strip().split()))
        res = nextLargestOptimized(arr, n)
        print(" ".join(stoi(x) for x in res))
