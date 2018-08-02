"""
567. Permutation in String

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

https://leetcode.com/problems/permutation-in-string/discuss/102604/%22Oneliners%22-in-Python-and-C++

https://leetcode.com/problems/permutation-in-string/discuss/102594/Python-Simple-with-Explanation

https://leetcode.com/problems/permutation-in-string/solution/

"""

# Result AC 108ms 38.12%


class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
        	return False

        A = [ord(x) - ord('a') for x in s1]
        B = [ord(x) - ord('a') for x in s2]

        target = [0] * 26
        for x in A:
        	target[x] += 1

        window = [0] * 26
        for i, x in enumerate(B):
            window[x] += 1
            if i >= len(A):
                window[B[i - len(A)]] -= 1
            if window == target:
                return True
        return False



if __name__ == '__main__':
    from time import time
    sol = Solution()
    t = time()
    ans = sol.checkInclusion("adc", "dcda")     
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))          		