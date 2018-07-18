"""
43. Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Ex.1
Input: num1 = "2", num2 = "3"
Output: "6"

Ex.2
Input: num1 = "123", num2 = "456"
Output: "56088"

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.


Thoughts:

1. Karatsuba Multiplication Modified?
2. Build in ascii convert, ord (). ord('0') is 48. Then you know how to do the rest.

"""

# Result: AC 48 ms 81.45%

class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1_int = num2_int = 0
        for d in num1:
        	num1_int = num1_int * 10 + (ord(d) - 48)
        for d in num2:
        	num2_int = num2_int * 10 + (ord(d) - 48)

        return (str(num1_int * num2_int))