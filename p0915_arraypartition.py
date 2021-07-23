"""
Given an array nums, partition it into two (contiguous) subarrays left and right so that:

    Every element in left is less than or equal to every element in right.
    left and right are non-empty.
    left has the smallest possible size.

Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.
"""

class Solution(object):
    def partitionDisjoint(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxval = 0
        acc = 0
        while True:
            cur_left = nums[0]
            cur_right = nums[1:]
            cur_min_right = min(cur_right)
            idx_min_right = cur_right.index(cur_min_right)
            # if left side is less than all of right side, we are done
            if max(maxval, cur_left) <= cur_min_right:
                return 1 + acc
            # if minimum of right side is less than entire left side, need to absorb it into left side
            else:
                cur_left = nums[:idx_min_right+1]
                cur_right = nums[idx_min_right+1:]
                maxval = max(maxval, max(cur_left))
                nums = cur_right
                acc += len(cur_left)