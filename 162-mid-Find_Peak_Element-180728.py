"""
162. Find Peak Element

A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.


<important>
Note:

Your solution should be in logarithmic complexity.
</important>
"""

"""
Follow up:

Top solution in leetcode actually traverse the list. However, this does not meet the log comlexity requirement.
"""


# Result 40ms 45.43%

class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        # Since complexity is required to be in log, use binary search instead of traverse
        while l <= r:
            mid = l + (r-l) // 2
            # Deal with length 1 or 2
            if (mid == 0 or nums[mid-1] < nums[mid]) and (mid == len(nums) - 1 or nums[mid] > nums[mid+1]):
                return mid;
            if nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                r = mid - 1