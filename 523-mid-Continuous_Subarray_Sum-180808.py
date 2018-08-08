"""
523. Continuous Subarray Sum

Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
Note:
The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.

https://leetcode.com/problems/continuous-subarray-sum/discuss/99516/Python-89ms-O(n)-time
https://leetcode.com/problems/continuous-subarray-sum/discuss/99499/Java-O(n)-time-O(k)-space
https://leetcode.com/problems/continuous-subarray-sum/discuss/99512/Python-with-explanation.-62ms-Time-O(min(n-k))-mostly
https://leetcode.com/problems/continuous-subarray-sum/discuss/99566/Simple-Python-(10-lines)-with-Explanation-58ms-O(n)-time-O(k)-space
https://leetcode.com/problems/continuous-subarray-sum/discuss/99575/Python-Simple-(Prefix-sum)
https://leetcode.com/problems/continuous-subarray-sum/discuss/99518/Not-smart-solution-but-easy-to-understand


"""

# Result AC 52ms 68.44%
# TBC 


class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        a = set([0, nums[0]])
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            if nums[i] == k == 0 or k and nums[i] % k in a:
                return True
            k and a.add(nums[i] % k)
        return False