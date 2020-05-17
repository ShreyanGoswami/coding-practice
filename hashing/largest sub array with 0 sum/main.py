# Given an array having both positive an negative integers. 
# The task is to complete the function maxLen() which returns the length of maximum subarray with 0 sum. 
# The function takes two arguments an array A and n where n is the size of the array A.
def maxLen(n, arr):
    prefixSum = [0] * n
    track = {arr[0]:0}
    prefixSum[0] = arr[0]
    maxLength = 0
    for i in range(1, n):
        prefixSum[i] = arr[i] + prefixSum[i-1]

        if prefixSum[i] == 0:
            if maxLength < i + 1:
                maxLength = i + 1
            continue
        if prefixSum[i] in track.keys():
            if maxLength < i - track[prefixSum[i]]:
                maxLength = i - track[prefixSum[i]]
        else:
            track[prefixSum[i]] = i
        
    return maxLength


if __name__ == '__main__':
    inp = input
    stoi = int
    itos = str
    t = stoi(inp())
    for i in range(t):
        n = stoi(inp())
        arr = list(map(stoi, inp().strip().split()))
        l = maxLen(n, arr)
        print(l)
