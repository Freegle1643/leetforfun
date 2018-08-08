"""
556. Next Greater Element III

Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:

Input: 12
Output: 21
 

Example 2:

Input: 21
Output: -1

https://leetcode.com/problems/next-greater-element-iii/discuss/101821/Python-39ms-O(n)
https://leetcode.com/problems/next-greater-element-iii/discuss/154503/Python-solution-same-as-next-permutation-problem
https://leetcode.com/problems/next-greater-element-iii/discuss/117208/Easy-Python3-beats-100

"""

# Result AC 36ms 67.94%


class Solution:
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [c for c in str(n)]
        for l in range(len(arr) - 2, -1, -1):
            r = len(arr) - 1
            while l < r and arr[r] <= arr[l]:
                r -= 1
            if l != r:
                arr[l], arr[r] = arr[r], arr[l]
                arr[l + 1:] = sorted(arr[l + 1:])
                num = int("".join(arr))
                return num if -2 ** 31 <= num <= 2 ** 31 - 1 else -1
        return -1