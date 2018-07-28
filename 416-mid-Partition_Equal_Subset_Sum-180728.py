"""
416. Partition Equal Subset Sum

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.


Thanks to ZhuEason

https://leetcode.com/problems/partition-equal-subset-sum/discuss/90592/01-knapsack-detailed-explanation/159315

"""

# Result TLE 104/104 passed


class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        l = len(nums)

        if l == 0:
        	return True
        if s % 2 != 0:
        	return False

        t = s // 2

        dp = [[False for j in range(t + 1)] for i in range(l + 1)]
        
        for j in range(1, t + 1):
        	dp[0][j] = False
        for i in range(1, l + 1):
            dp[i][0] = True
        dp[0][0] = True

        for i in range(1, l + 1):
        	for j in range(1, t + 1):
        		if j >= nums[i - 1]:
        			dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
        		else:
        			dp[i][j] = dp[i - 1][j]
        return dp[l][t]

