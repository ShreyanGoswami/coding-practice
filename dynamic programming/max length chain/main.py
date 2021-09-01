# You are given N pairs of numbers. In every pair, the first number is always smaller than the second number.
# A pair (c, d) can follow another pair (a, b) if b < c. Chain of pairs can be formed in this fashion.
# Your task is to complete the function maxChainLen which returns an integer denoting the longest chain which can be formed from a given set of pairs.


class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def maxChainLen(Parr, n):
    # Parr:  list of pair
    Parr.sort(key=lambda x: x.a)
    dp = [0] * n
    dp[0] = 1
    for i in range(1, n):
        maxLengthAtI = 0
        for j in range(i):
            if Parr[i].a > Parr[j].b and dp[j] > maxLengthAtI:
                maxLengthAtI = dp[j]
        dp[i] = 1 + maxLengthAtI

    return max(dp)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        Parr = []
        i = 0
        while n * 2 > i:
            Parr.append(Pair(arr[i], arr[i + 1]))
            i += 2
        print(maxChainLen(Parr, n))
