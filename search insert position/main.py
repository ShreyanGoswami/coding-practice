"""
Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        while start < end:
            mid = (start + end) >> 1
            if nums[mid] == target:
                return mid
            elif mid != 0 and nums[mid - 1] < target < nums[mid]:
                return mid
            elif mid != end - 1 and nums[mid] < target < nums[mid + 1]:
                return mid + 1
            elif nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
        return start


if __name__ == "__main__":
    s = Solution()
    print(s.searchInsert([1, 3, 5, 6, 8], 9))
