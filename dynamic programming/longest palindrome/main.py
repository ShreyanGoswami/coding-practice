# Given a string S, find the longest palindromic substring in S. Substring of string S: S[ i . . . . j ] where 0 ≤ i ≤ j < len(S). 
# Palindrome string: A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S. 
# Incase of conflict, return the substring which occurs first ( with the least starting index ).
# Return the first character of the input string if no palindrome sequence is found

def longestPalindrome(s):
    rs = s[::-1]
    n = len(s)
    dp = []
    for i in range(0, n + 1):
        dp.append([0] * (n + 1))
    for i in range(1, n+1):
        for j in range(1, n+1):
            if rs[i-1] == s[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
    
    maxVal = 0
    iIndex = 0
    jIndex = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dp[i][j] >= maxVal:
                maxVal  = dp[i][j]
                iIndex = i
                jIndex = j
    if maxVal == 0 or maxVal == 1:
        return s[0]
    else:
        op = ''
        while iIndex > 0 and dp[iIndex][jIndex] > 0:
            op += s[jIndex-1]
            iIndex -= 1
            jIndex -= 1
        if op == op[::-1]:
            return op
        else:
            return s[0]


if __name__ == '__main__':
    inp = input
    itos = int
    t = itos(inp())
    for i in range(t):
        str1 = inp().strip()
        res = longestPalindrome(str1)
        print(res)

