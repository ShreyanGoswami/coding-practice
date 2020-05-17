from typing import List
####
# Maximum subarray
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
####

# Solution: Using Kadane's algorithm
# The idea is that the maximum sub array will be the current element  + the maximum subarray of the previous contiguous elements just before the current element

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        originalLength = len(nums)
        maxSum = currSum = nums[0]
        for i in range(1, originalLength):
            currSum = self.findMax(nums[i], nums[i] + currSum)
            if currSum > maxSum:
                maxSum = currSum
        return maxSum
    
    def findMax(self, i: int, j: int) -> int:
        if i > j:
            return i
        return j



nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [-2]

sol = Solution()
print(sol.maxSubArray(nums))
