from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = []
        numCoins = len(coins)
        for i in range(numCoins + 1):
            dp.append([0] * (amount + 1))
        row = 1
        for c in coins:
            if row < numCoins + 1 and c <= amount:
                dp[row][c] = 1
                row += 1
            else:
                break

        for i in range(1, numCoins + 1):
            for j in range(1, amount + 1):
                if j > coins[i - 1]:
                    dp[i][j] = dp[i][j] + dp[i][j - coins[i - 1]] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j] + dp[i - 1][j]
        return dp[len(coins)][amount]


if __name__ == "__main__":
    s = Solution()
    print(s.change(5, [1, 2, 5]))
    print(s.change(4, [1, 2, 5]))
    print(s.change(3, [1, 2, 5]))
    print(s.change(2, [1, 2, 5]))
