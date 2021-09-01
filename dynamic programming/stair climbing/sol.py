# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# define a 1D array that tracks how many different ways are there given a certain number of steps. It will be built bottom up.


class Solution:
    def climbStairs(self, n: int) -> int:
        diffWaysTotal = {0: 0, 1: 1, 2: 2}
        self.recursive_optimal(n, diffWaysTotal)
        return diffWaysTotal[n]

    def recursive(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.recursive(n - 1) + self.recursive(n - 2)

    def recursive_optimal(self, n, cache):
        if n in cache:
            return cache[n]
        else:
            differentWaysWithOneStep = self.recursive_optimal(n - 1, cache)
            differentWaysWithTwoStep = self.recursive_optimal(n - 2, cache)
            cache[n] = differentWaysWithOneStep + differentWaysWithTwoStep
            return cache[n]


sol = Solution()
print(sol.climbStairs(4))
