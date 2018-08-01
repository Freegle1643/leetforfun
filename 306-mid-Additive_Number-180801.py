"""
306. Additive Number

Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Example 1:

Input: "112358"
Output: true 
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
Example 2:

Input: "199100199"
Output: true 
Explanation: The additive sequence is: 1, 99, 100, 199. 
             1 + 99 = 100, 99 + 100 = 199
Follow up:
How would you handle overflow for very large input integers?
"""


class Solution:
    def isAdditiveNumber(self, num):
        if len(num) < 3:
            return False
        for i in range(len(num) // 2):
        	# len(num) // 3 * 2 cuz there would be a third number equals to one + two
            for j in range(i+1, len(num) // 3 * 2):
                one = int(num[:i+1])
                two = int(num[i+1:j+1])
                if self.generate_fib_str(one, two, len(num)) == num:
                    return True
                if num[j] == 0:
                    break
            if num[0] == '0':
                break
        return False
    
    def generate_fib_str(self, a, b, n):
        # type: int, int, int -> str
        fib_str = str(a) + str(b)
        while len(fib_str) < n:
            fib_str += str(a + b)
            a, b = b, a+b
        return fib_str[:n]