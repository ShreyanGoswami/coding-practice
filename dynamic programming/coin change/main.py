# Given a value N, find the number of ways to make change for N cents, if we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins.
# The order of coins doesn’t matter. For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}.
# So output should be 4. For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.


def totalWays(arr, n, k):
    dp = []
    for i in range(n + 1):
        dp.append([0] * (k + 1))

    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            # At every point you have the option of picking the coin(stay in the same row) or don't pick the coin(move to previous row)
            if j >= arr[i - 1]:
                dp[i][j] = dp[i][j - arr[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][k]


if __name__ == "__main__":
    inp = input
    stoi = int
    t = stoi(inp())
    for i in range(t):
        n = stoi(inp())
        arr = list(map(stoi, inp().strip().split()))
        k = stoi(inp())
        print(totalWays(arr, n, k))
