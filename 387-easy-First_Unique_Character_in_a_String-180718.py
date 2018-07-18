"""
387. First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Ex.
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.

Thoughts:
1. Since we need to find non-repeating charactor, a go-through over the whole string is definitely needed (O(n)). 
2. Index of a character is required to return, we need a container data structure that supports order.(Not entirely necessary though, but good to have).
3. In worst case, the size of list is the same size as input string. But we only need to output the first non-repeating character.
4. In my solution, 0 represents that this character fits the need. This does NOT represent the amount.

"""

# Result: AC 116 ms 70.55%

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        worker = dict([])
        for c in s:
        	if c not in worker:
        		worker[c] = 0
        	elif c in worker:
        		worker[c] = 1
        for i in range(len(s)):
        	if worker[s[i]] == 0:
        		return i
        return -1