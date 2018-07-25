"""
345. Reverse Vowels of a String

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
"""

# Result 


class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        v_ori = []
        for i in s:
        	if i in vowels:
        		v_ori.append(i)

        k = 0

        l = len(s)
        for j in range(l - 1, -1, -1):
        	if s[j] in vowels:
        		s = s[:j] + v_ori[k] + s[j + 1:]
        		k += 1

        return s


if __name__ == '__main__':
	from time import time
	sol = Solution()
	t = time()
	ans = sol.reverseVowels('leotcede')
	print('ans: %s\ntime: %.3fms' % (ans, (time() - t) * 1000)) 