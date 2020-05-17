# Given a sequence A of size N, find the length of the longest increasing subsequence from a given sequence .
# The longest increasing subsequence means to find a subsequence of a given sequence in which the subsequence's elements are in sorted order, 
# lowest to highest, and in which the subsequence is as long as possible. 
# This subsequence is not necessarily contiguous, or unique.
# Note: Duplicate numbers are not counted as increasing subsequence.

def lis(arr, n):
    dp = [0] * n
    dp[0] = 1
    for i in range(1, n):
        maxLengthAtI = 0
        for j in range(0, i):
            if arr[j] < arr[i] and maxLengthAtI < dp[j]:
                maxLengthAtI = dp[j]
        dp[i] = 1 + maxLengthAtI
    return max(dp)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        inp = list(map(int, input().strip().split()))
        print(lis(inp, n))