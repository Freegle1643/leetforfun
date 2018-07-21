"""
49. Group Anagrams

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

"""

# Result: AC 124ms 83.62%

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anas = {}
        for string in strs:
            s = ''.join(sorted(string))
            if s in anas:
                anas[s].append(string)
            else:
                anas[s] = [string]
        return [ anas[x] for x in anas ]