# Given two strings str1 and str2 and below operations that can performed on str1.
# Find minimum number of edits (operations) required to convert ‘str1′ into ‘str2′.
# Insert
# Remove
# Replace
# All of the above operations are of cost=1.
# Both the strings are of lowercase.
def editDistance(str1, str2, n1, n2):
    dp = []
    for i in range(n1 + 1):
        dp.append([0] * (n2 + 1))
    dp[0] = [i for i in range(n2 + 1)]
    for i in range(1, n1 + 1):
        dp[i][0] = dp[i - 1][0] + 1

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])

    return dp[n1][n2]


if __name__ == "__main__":
    inp = input
    itos = int
    t = itos(inp())
    for i in range(t):
        l = list(map(itos, inp().strip().split()))
        n1, n2 = l[0], l[1]
        l = inp().strip().split()
        str1 = l[0]
        str2 = l[1]
        print(editDistance(str1, str2, n1, n2))
