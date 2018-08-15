"""
491. Increasing Subsequences

Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2 .

Example:
Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
Note:
The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.

https://leetcode.com/problems/increasing-subsequences/discuss/97157/DP-solution:-not-as-clean-as-other-Python-solutions-but-beats-99-in-speed
https://leetcode.com/problems/increasing-subsequences/discuss/97127/Simple-Python
https://leetcode.com/problems/increasing-subsequences/discuss/97197/Python-solution-by-easily-checking-all-combinations

"""

# Result AC 552ms 8.06%
# SLOW

import itertools


class Solution:
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(2, len(nums)+1):
        	res.extend(set(itertools.combinations(nums, i)))
        return [x for x in res if self.isIncreasing(x)]

    def isIncreasing(self, sub):
    	for i in range(1, len(sub)):
    		if sub[i-1] > sub[i]:
    			return False
    	return True