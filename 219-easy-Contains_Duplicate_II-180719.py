"""
219. Contains Duplicate II

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Ex.

Input: nums = [1,2,3,1], k = 3
Output: true

Input: nums = [1,0,1,1], k = 1
Output: true

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Thoughts:
<abandoned>
1. First determine wether there are duplicate numbers. Using set() to compare len()
	! Time costly !
2. Go through the array, use a list of list(Not a dict, since the order we are not able to control. But we use is like a dict). 
3. If any first element(key) has a second element (value) more that 1, compare current j and key index i with k.
</abandoned>

1. Use window with len()==k to go through the array

"""

# Resul: AC 64 ms 16.10%

from collections import deque,defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0:
        	return False

        seen_num = deque(maxlen = k)
        que_cnt = defaultdict(int)

        for num in nums:
        	if que_cnt[num]:
        		return True
        	if len(seen_num) == k:
        		left_num = seen_num.popleft()
        		que_cnt[left_num] -= 1

        	seen_num.append(num)
        	que_cnt[num] += 1   

        return False    			

if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.containsNearbyDuplicate([1,2,3,2,1,3],2)
    print('ans: %s\ntime: %.3fms' % (ans and ans, ((time() - t)) * 1000))   