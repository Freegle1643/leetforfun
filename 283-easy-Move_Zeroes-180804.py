"""
283. Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

# Result AC 48ms 97.42%


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        z_holder = 0
        for i in range(len(nums)):
        	if nums[i] != 0:
        		nums[z_holder], nums[i] = nums[i], nums[z_holder]
        		z_holder += 1

