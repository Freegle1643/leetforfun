"""
260. Single Number III

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

"""

# Result: AC 44ms 64.80%


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
        s1 = cnt.popitem()[0]
        s2 = cnt.popitem()[0]
        return [s1,s2]


if __name__ == '__main__':
    from time import time
    sol = Solution()
    t = time()
    ans = sol.singleNumber([1,2,1,3,2,5])
    print('ans: %s\ntime: %.3fms' % (ans, (time() - t) * 1000))  