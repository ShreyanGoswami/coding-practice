from typing import List


class Solution:
    def kadane(self, arr):
        prevSum = next(arr)
        maxSum = prevSum
        for x in arr:
            prevSum = max(prevSum + x, x)
            maxSum = max(prevSum, maxSum)
        return maxSum

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        k = self.kadane(iter(A))
        totalSum = sum(A)
        r = (x * -1 for x in A)
        kComplement = self.kadane(r)
        totalSum = totalSum + kComplement
        if totalSum > k and totalSum != 0:
            return totalSum
        return k


if __name__ == "__main__":
    s = Solution()
    print(s.maxSubarraySumCircular([1, -2, 3, -2]))
    print(s.maxSubarraySumCircular([5, -3, 5]))
    print(s.maxSubarraySumCircular([3, -1, 2, -1]))
    print(s.maxSubarraySumCircular([3, -2, 2, -3]))
    print(s.maxSubarraySumCircular([-2, -3, -1]))
