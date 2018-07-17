"""
316. Remove Duplicate Letters

Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Ex.1

Input: "bcabc"
Output: "abc"

Note:
1. The wrong answer output info makes no sense to me. More understand on the order is required. 

"""

# Result: Wrong answer
# 143 / 286 Passed, Others are wrong TBC

from collections import OrderedDict

class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmp = "".join(OrderedDict.fromkeys(s))
        return (''.join(sorted(tmp)))