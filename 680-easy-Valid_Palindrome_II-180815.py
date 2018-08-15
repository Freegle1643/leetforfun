"""
680. Valid Palindrome II

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

"""

# Result AC 120ms 72.81%


class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        while left < right:
        	if s[left] != s[right]:
        		first, second = s[left:right], s[left+1:right+1]
        		return first == first[::-1] or second == second[::-1]
        	left, right = left + 1, right - 1
        return True