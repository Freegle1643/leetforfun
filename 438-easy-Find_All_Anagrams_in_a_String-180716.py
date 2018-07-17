"""
438. Find All Anagrams in a String

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Ex.1

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Note:

1. Pattern contains duplicate charactor
2. Copy but not edit the original object in Python
3. Initialize fixed size dict/set etc. (TBC)

"""

# Result: Timeout
# 34/36 Passed, 2/36 Timeout TBC

from collections import defaultdict

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        if len(s)<len(p) :
            return []

        # We use two dictionary dp/dt and ds, dp is initialized with all values equal to the amount of a alphabet.
        # If we find a match charactor, the value of corresponding key-value pair in dp would decrease by 1.
        # If after len(p) steps, all the values in dp are 0, put corresponding index of s in result.

        dp = defaultdict(int)

        for i in range(len(p)) :
            dp[p[i]] = int(dp[p[i]]) + 1

        results = []

        for j in range(0, len(s)-len(p)+1):
            if s[j] in dp:
                dt = dp.copy()
                dt[s[j]] -= 1 # cross that charactor in this run

                t = j + 1

                for k in range(len(p) - 1):
                    if s[t] in dt and dt[s[t]] != 0: # another charactor match and it has not been crossed
                        dt[s[t]] -= 1
                        t += 1


                if t - j == len(p): # successfully cross len(p) charactors
                    results.append(j)

        return results


                        
if __name__ == '__main__':
    print(Solution().findAnagrams('baa', 'aa'))