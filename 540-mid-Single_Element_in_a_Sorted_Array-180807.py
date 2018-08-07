"""
540. Single Element in a Sorted Array

Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10
Note: Your solution should run in O(log n) time and O(1) space.

Thoughts:
O(log n): Binary Search

"""


class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, h = 0 , len(nums)-1
        while (l<h):
            m = l + (h-l)//2
            if (nums[m]!=nums[m+1] and nums[m]!=nums[m-1]):
                return nums[m]
            elif (m%2 ==1 and nums[m]==nums[m-1]):
                l = m+1
            elif (m%2 ==0 and nums[m]==nums[m+1]):
                l = m+1
            else:
                h = m-1
        return nums[l]