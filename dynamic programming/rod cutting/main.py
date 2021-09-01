# Given an integer N denoting the Length of a line segment. you need to cut the line segment in such a way that
# the cut length of a line segment each time is integer either x , y or z.
# After performing all cutting operation the total number of cutted segments must be maximum.


def findMaxCutsRecurs(n, x, y, z, dp):
    # Will not work if the height of recursion is more than 1000
    if n < 0:
        return -1
    if dp[n] != -2:
        return dp[n]
    if n == 0:
        return 0
    cutx = findMaxCuts(n - x, x, y, z, dp)
    cuty = findMaxCuts(n - y, x, y, z, dp)
    cutz = findMaxCuts(n - z, x, y, z, dp)
    if cutx == -1 and cuty == -1 and cutz == -1:
        return -1
    dp[n] = 1 + max(cutx, cuty, cutz)
    return dp[n]


def getCut(n, c, dp):
    if n - c < 0:
        return -1
    if dp[n - c] != -2:
        return dp[n - c]
    if n - c == 0:
        return 0


def findMaxCuts(n, x, y, z, dp):
    for i in range(1, n + 1):
        cutx = getCut(i, x, dp)
        cuty = getCut(i, y, dp)
        cutz = getCut(i, z, dp)
        if cutx == -1 and cuty == -1 and cutz == -1:
            dp[i] = -1
            continue
        dp[i] = 1 + max(cutx, cuty, cutz)
    return dp[n]


def main():
    t = int(input())
    for i in range(0, t):
        n = int(input())
        l = input().strip().split(" ")
        x, y, z = int(l[0]), int(l[1]), int(l[2])
        dp = [-2] * (n + 1)
        sol = findMaxCuts(n, x, y, z, dp)
        print(sol)


main()
