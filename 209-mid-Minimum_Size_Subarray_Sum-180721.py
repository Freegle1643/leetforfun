"""
209. Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
"""

# Result: AC 44ms 99.82%


class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        min_len = 9999999999
        left = 0
        worker = 0

        for i in range(len(nums)):
            worker += nums[i]
            while worker >= s:
                min_len = min(i - left, min_len)
                worker -= nums[left]
                left += 1
        return min_len if min_len != 9999999999 else 0


if __name__ == '__main__':
    from time import time
    sol = Solution()
    t = time()
    ans = sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3, 7])
    print('ans: %s\n time: %.3fms' % (ans, (time() - t) * 1000))