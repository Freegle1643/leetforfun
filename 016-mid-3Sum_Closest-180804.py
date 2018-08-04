"""
16. 3Sum Closest

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

# Result AC 132ms 44.97%


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
        	j, k = i+1, len(nums) - 1
        	while j < k:
        		sum_n = nums[i] + nums[j] + nums[k]
        		if sum_n == target:
        			return sum_n
        		if abs(sum_n - target) < abs(res - target):
        			res = sum_n
        		if sum_n < target:
        			j += 1
        		elif sum_n > target:
        			k -= 1

        return res