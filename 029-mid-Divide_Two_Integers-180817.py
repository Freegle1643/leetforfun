"""
29. Divide Two Integers

Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

Note:
1. https://leetcode.com/problems/divide-two-integers/discuss/13565/Python-devs-be-wary-of-the-integer-of-division-of-a-positive-and-a-negative-number
	dividend//divisor returned a lot of result that could not pass the OJ, link above explaned
2. Bitwise Operators https://wiki.python.org/moin/BitwiseOperators
	x >> y
	Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.


"""

# Result AC 52ms 100%
# TBC


class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)