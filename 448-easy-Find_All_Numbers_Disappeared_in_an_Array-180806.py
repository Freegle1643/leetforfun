"""
448. Find All Numbers Disappeared in an Array

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

# Result AC 360 ms 2.64%
# You would suffer time comlexity if not suffer space

"""
class Solution:
    def findDisappearedNumbers(self, nums):
        new_one = [True]*(len(nums)+1)
        new_one[0] = False 
        for i in nums:
            new_one[i] = False
        return [i for i, x in enumerate(new_one) if x]
"""


class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
        	return []
        nums.sort()
        res = []
        i = len(nums)
        j = i - 1
        print(nums)
        while j >= 0:
        	print('No. ',j, 'num = ',nums[j])
        	print('i: ',i)
        	if i == nums[j]:
        		if j > 0:
        			# occur twice
        			if i == nums[j-1]:
        				print('twice')
        				j -= 2
        				if j < 0 and i != 1:
        					for x in range(1,i):
        						res.append(x)
        					print(res)
        			# occur once
        			else:
        				print('once')
        				j -= 1
        		else:
        			if i != 1:
	        			for x in range(1,i):
	        				res.append(x)
	        			print(res)
	        		break
        		i -= 1
        	else:
        		while nums[j] != i:
        			res.append(i)
        			print(res)
        			i -= 1
        
        return res


if __name__ == '__main__':
    from time import time
    sol = Solution()
    t = time()
    ans = sol.findDisappearedNumbers([4,3,2,7,8,2,3,1])     
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))  