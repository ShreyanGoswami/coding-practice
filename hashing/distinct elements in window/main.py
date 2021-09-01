# Given an array A[] of size N and an integer K.
# Your task is to complete the function countDistinct() which prints the count of distinct numbers in all windows of size k in the array A[].
def getDisintctCount(arr, n, k):
    d = {}
    res = []
    itos = str
    start = 0
    end = k
    temp = start
    while end < n:
        while temp != end:
            try:
                d[arr[temp]] += 1
            except KeyError:
                d[arr[temp]] = 1
            temp += 1
        res.append(len(d.keys()))
        d[arr[start]] -= 1
        if d[arr[start]] == 0:
            del d[arr[start]]
        start += 1
        end += 1
    temp = start
    while temp != end:
        try:
            d[arr[temp]] += 1
        except KeyError:
            d[arr[temp]] = 1
        temp += 1
    res.append(len(d.keys()))
    print(" ".join(itos(x) for x in res))


if __name__ == "__main__":
    inp = input
    stoi = int
    t = stoi(inp())
    for i in range(t):
        l = list(map(stoi, inp().strip().split()))
        n, k = l[0], l[1]
        arr = list(map(stoi, inp().strip().split()))
        getDisintctCount(arr, n, k)
