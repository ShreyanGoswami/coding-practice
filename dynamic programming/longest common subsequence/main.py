# TODO Fix it
def longestCommonSubsequence(str1, str2, n1, n2):
    dp = []
    d = {}
    s = []
    maxLength = 0
    positionOfMaxLength = 0
    for i in range(n2 + 1):
        dp.append([0] * (n1 + 1))

    for x in str2:
        d[x] = 1

    for i in range(1, n2 + 1):
        isFound = False
        hits = 1
        for j in range(1, n1 + 1):
            if str2[i - 1] == str1[j - 1] and isFound == False:
                if d[str2[i - 1]] == hits:
                    dp[i][j] = 1 + max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                    s.append(str2[i - 1])
                    print("Found character at position", i, " ", j)
                    d[str2[i - 1]] += 1
                    isFound = True
                else:
                    hits += 1
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return len(s)


if __name__ == "__main__":
    inp = input
    itos = int
    t = itos(inp())
    for i in range(t):
        l = list(map(itos, inp().strip().split()))
        n1, n2 = l[0], l[1]
        str1 = inp().strip()
        str2 = inp().strip()
        print(longestCommonSubsequence(str1, str2, n1, n2))
