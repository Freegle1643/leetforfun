"""
670. Maximum Swap

Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108]
"""

# Result AC 36ms 96.27%


class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = 0
        digits = [10**i for i in range(len(str(num)))]
        for p in digits:
        	for q in digits:
        		res = max(res, num + num//p%10 * (q-p) + num//q%10 * (p-q))
        return res
