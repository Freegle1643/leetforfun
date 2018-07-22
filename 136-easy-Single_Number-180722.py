"""
136. Single Number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

# Result AC 44ms 71.74%


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = {}
        for num in nums:
        	if num in cnt:
        		cnt[num] = 0
        		del cnt[num]
        	else:
        		cnt[num] = 1
        single = cnt.popitem()[0]
        return single


if __name__ == '__main__':
    from time import time
    sol = Solution()
    t = time()
    ans = sol.singleNumber([4,1,2,1,2])
    print('ans: %s\ntime: %.3fms' % (ans, (time() - t) * 1000))       