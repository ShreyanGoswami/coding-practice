# Given an array arr of N integers. Find the contiguous sub-array with maximum sum.


def maxSum(arr, n):
    s = [arr[0]]
    for i in range(1, n):
        t = s[i - 1] + arr[i]
        s.append(max(t, arr[i]))
    return max(s)


if __name__ == "__main__":
    inp = input
    stoi = int
    t = stoi(inp())
    for _ in range(t):
        n = stoi(inp())
        arr = list(map(stoi, inp().strip().split()))
        print(maxSum(arr, n))
