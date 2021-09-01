def findMaxValue(n, v, w, W):
    dp = []
    for i in range(n):
        dp.append([0] * (W + 1))

    if w[0] <= W:
        for i in range(w[0], W + 1):
            dp[0][i] = v[0]

    for i in range(1, n):
        for j in range(0, W + 1):
            if w[i] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])
    return dp[n - 1][W]


if __name__ == "__main__":
    inp = input
    stoi = int

    t = stoi(inp())
    for i in range(t):
        n = stoi(inp())
        W = stoi(inp())
        v = list(map(stoi, inp().strip().split()))
        w = list(map(stoi, inp().strip().split()))
        print(findMaxValue(n, v, w, W))
