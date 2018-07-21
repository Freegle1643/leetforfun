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

from collections import deque

class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 1 and nums[0] != s:
            print('false')
            return 0

        worker = deque()
        min_len = 0
        for num in nums:
            print('continue')
            worker.append(num)
            print('before', worker, min_len)
            if sum(worker) >= s:
                print('>=')
                min_len = len(worker)
                if sum(worker) == s:
                    print('=')
                    if len(worker) < min_len:
                        min_len = len(worker)
                if sum(worker) > s:
                    print('>')
                    while worker:
                        worker.popleft()
                        print('worker poped',worker, sum(worker))
                        if sum(worker) >= s:
                            print('new match')
                            if len(worker) < min_len:
                                min_len = len(worker)
                        if sum(worker) < s:
                            print('woker poped done')
                            break

        	# if sum(worker) == s:
        	# 	print('equal')
            if len(worker) < min_len:
                min_len = len(worker)



            print('after', worker, min_len,'\n')
        	# if sum(worker) < s:
        	# 	worker.append(num)

        return min_len


if __name__ == '__main__':
    from time import time
    sol = Solution()
    t = time()
    ans = sol.minSubArrayLen(7,[2, 3, 1, 2, 4, 3, 4, 8])
    # ans = sol.minSubArrayLen(11,[1,2,3,4,5])
    # ans = sol.minSubArrayLen(15,[5,1,3,5,10,7,4,9,2,8])
    # ans = sol.minSubArrayLen(11,[1])
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
