"""
458. Poor Pigs


There are 1000 buckets, one and only one of them contains poison, the rest are filled with water. They all look the same. If a pig drinks that poison it will die within 15 minutes. What is the minimum amount of pigs you need to figure out which bucket contains the poison within one hour.

Answer this question, and write an algorithm for the follow-up general case.

Follow-up:

If there are n buckets and a pig drinking poison will die within m minutes, how many pigs (x) you need to figure out the "poison" bucket within p minutes? There is exact one bucket with poison.

https://leetcode.com/problems/poor-pigs/discuss/94266/Another-explanation-and-solution

Improved:

def poorPigs(self, buckets, minutesToDie, minutesToTest):
    pigs = 0
    while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
        pigs += 1
    return pigs

"""

# Result AC 20ms 91.47%


class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        if minutesToTest <= minutesToDie:
        	return 0

        factor = minutesToTest//minutesToDie + 1
        pigs = 1
        maxbuckets = 0
        while True:
        	maxbuckets = factor ** pigs
        	if maxbuckets >= buckets:
        		return pigs
        	pigs += 1