"""
354. Russian Doll Envelopes

You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Example:
Given envelopes = [[5,4],[6,4],[6,7],[2,3]], the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

https://leetcode.com/problems/russian-doll-envelopes/discuss/82754/Python-solution-based-on-LIS
https://leetcode.com/problems/longest-increasing-subsequence/solution/



"""

# Result AC 84ms 61.70%

import bisect


class Solution:
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        des_ht = [a[1] for a in sorted(envelopes, key = lambda x: (x[0], -x[1]))]
        print(des_ht)
        dp, l = [0] * len(des_ht), 0
        for x in des_ht:
            i = bisect.bisect_left(dp, x, 0, l)
            dp[i] = x
            print(dp)
            print('i',i,'dp[i]',dp[i],'l',l)
            if i == l:
                l+=1
        return l
        				

if __name__ == '__main__':
    from time import time
    sol = Solution()
    t = time()
    ans = sol.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]])     
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))          				