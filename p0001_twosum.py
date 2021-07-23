"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,n in enumerate(nums):
            for j,m in enumerate(nums[i+1:]):
                j += i+1 # index offset from start of array
                if n+m == target:
                    return [i,j]

# better solution: keep a dictionary. For each element nums[i], if it is not a key in dict, store key,val pair (target - nums[i], i).
# Then it is O(n). (Mine is O(n^2))