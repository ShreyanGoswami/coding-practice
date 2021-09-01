# Given an array of integers where each element represents the max number of steps that can be made forward from that element.
# The task is to find the minimum number of jumps to reach the end of the array (starting from the first element).
# If an element is 0, then cannot move through that element.


def minSteps(arr, n):
    dp = [0] * n
    if arr[0] == 0:
        return -1
    if arr[0] >= n:
        return 1
    for i in range(1, n):
        minSteps = -1
        if arr[i] == 0 and i != n - 1:
            continue
        for j in range(i):
            if j + arr[j] >= i and minSteps == -1:
                minSteps = dp[j]
            elif j + arr[j] >= i and minSteps != -1 and dp[j] < minSteps:
                minSteps = dp[j]
        dp[i] = 1 + minSteps
        if arr[i] + i >= n - 1 and i != n - 1:
            dp[n - 1] = 1 + dp[i]
            break
    if dp[n - 1] != 0:
        return dp[n - 1]
    return -1


if __name__ == "__main__":
    t = int(input())
    inp = input
    intF = int
    for i in range(0, t):
        n = int(input())
        l = list(map(intF, inp().strip().split(" ")))
        print(minSteps(l, n))
