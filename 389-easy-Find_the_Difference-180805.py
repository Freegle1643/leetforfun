"""
389. Find the Difference

Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.


https://leetcode.com/problems/find-the-difference/discuss/86881/Python-solution-which-beats-96
https://leetcode.com/problems/find-the-difference/discuss/86904/3-Different-Python-Solutions-(Dictionary-Difference-XOR)
https://leetcode.com/problems/find-the-difference/discuss/86845/1-liners-and-2-liner-in-Python
"""


class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = {}
        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1
        for ch in t:
            if dic.get(ch, 0) == 0:
                return ch
            else:
                dic[ch] -= 1