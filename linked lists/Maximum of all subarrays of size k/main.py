# Given an array A and an integer K. Find the maximum for each and every contiguous subarray of size K.
def findLargest(arr, n, k):
    stoi = int
    if len(arr) < k:
        print(max([stoi(x) for x in arr]))
        return
    start = 0
    end = k - 1
    maxEle = -1
    while end < n:
        if maxEle == -1:
            temp = [stoi(x) for x in arr[start:end+1]]
            maxEle = max(temp)
        else:
            if maxEle < stoi(arr[end]):
                maxEle = stoi(arr[end])
            elif stoi(arr[start - 1]) == maxEle:
                temp = [stoi(x) for x in arr[start:end+1]]
                maxEle = max(temp)

        print(maxEle, end = ' ')
        start += 1
        end += 1
            
if __name__ == '__main__':
    inp = input
    itos = str
    stoi = int
    t = stoi(inp())
    for i in range(t):
        l = list(map(stoi, inp().strip().split()))
        n, k = l[0], l[1]
        arr = inp().strip().split()
        findLargest(arr, n, k)
        print()