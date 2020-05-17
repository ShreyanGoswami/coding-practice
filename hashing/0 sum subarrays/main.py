# You are given an array A of size N. You need to print the total count of sub-arrays having their sum equal to 0

def lenOfZeroSumSubArrays(arr, n):
    d = {arr[0]:[0]}
    prefixSum = [arr[0]]
    if arr[0] == 0:
        count = 1
    else:
        count = 0
    for i in range(1, n):
        prefixSum.append(arr[i] + prefixSum[i-1])
        if prefixSum[i] == 0:
            count += 1

        if prefixSum[i] in d.keys():
            count += len(d[prefixSum[i]])
            d[prefixSum[i]].append(i)
        else:
            d[prefixSum[i]] = [i]

    return count

if __name__ == '__main__':
    inp = input
    stoi = int
    itos = str
    t = stoi(inp())
    for i in range(t):
        n = stoi(inp())
        arr = list(map(stoi, inp().strip().split()))
        print(lenOfZeroSumSubArrays(arr, n))
