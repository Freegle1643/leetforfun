"""
91. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

"""

# Result AC 72ms 2.28%
# TBC


class Solution:
    
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) == 0: return 0
        if len(s) == 1: return 0 if int(s) == 0 else 1
        
        next2 = 1 if int(s[-1]) != 0 else 0
        next1 = (next2 if int(s[-2]) != 0 else 0) + (1 if 10 <= int(s[-2:]) <= 26 else 0)
        for i in range(len(s)-3, -1, -1):
            curr = (next1 if int(s[i]) != 0 else 0) + (next2 if 10 <= int(s[i:i+2]) <= 26 else 0)   
            next1, next2 = curr, next1
        return next1