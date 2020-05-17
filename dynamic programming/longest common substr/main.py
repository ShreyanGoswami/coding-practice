def longestCommonSubstr(str1, str2, n1, n2):
    if n1 == 0 or n2 == 0:
        return 0
    dp = []
    for i in range(n2 + 1):
        dp.append([0] * (n1 + 1))
    
    for i in range(1, n2 + 1):
        for j in range(1, n1 + 1):
            if str2[i-1] == str1[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
    maxLength = 0
    for i in range(1, n2 + 1):
        if maxLength < max(dp[i]):
            maxLength = max(dp[i])
    return maxLength

if __name__ == '__main__':
    inp = input
    itos = int
    t = itos(inp())
    for i in range(t):
        l = list(map(itos, inp().strip().split()))
        n1, n2 = l[0], l[1]
        str1 = inp().strip()
        str2 = inp().strip()
        print(longestCommonSubstr(str1, str2, n1, n2))