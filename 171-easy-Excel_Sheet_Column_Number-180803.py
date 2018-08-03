"""
171. Excel Sheet Column Number

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701


Better: 100%

    def titleToNumber(self, s):
        result, start = 0, ord('A')
        for c in s:
            result = result * 26 + (ord(c) - start) + 1
        return result



"""

# Result AC 64 ms 21.53%


class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        alpha2num = { 
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9,
        "J": 10,
        "K": 11,
        "L": 12,
        "M": 13,
        "N": 14,
        "O": 15,
        "P": 16,
        "Q": 17,
        "R": 18,
        "S": 19,
        "T": 20,
        "U": 21,
        "V": 22,
        "W": 23,
        "X": 24,
        "Y": 25,
        "Z": 26
        }

        n = len(s)
        num = 0
        for i in range(n-1, -1, -1):
        	num += alpha2num[s[i]] * (26 ** (n - 1 - i))
        return num