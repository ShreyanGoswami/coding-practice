from typing import List

####
# Maximum subarray
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
####


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        max_sum = (2 ** 31 - 1) * (-1)
        while size > 0:
            for i in range(0, len(nums)):
                end = i + size
                if end <= len(nums):
                    temp = nums[i:end]
                    temp_sum = sum(temp)
                    if temp_sum > max_sum:
                        max_sum = temp_sum
            size = size - 1
        return max_sum


# nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [-2]
sol = Solution()
print(sol.maxSubArray(nums))
