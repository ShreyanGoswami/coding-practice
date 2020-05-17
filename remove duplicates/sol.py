from typing import List
# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        curr_len = len(nums)
        while i < curr_len:
            if nums[i] == nums[i-1]:
                nums.pop(i)
                curr_len = curr_len - 1
                i = i - 1
            i = i + 1
        return curr_len

nums = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()
print(sol.removeDuplicates(nums))
