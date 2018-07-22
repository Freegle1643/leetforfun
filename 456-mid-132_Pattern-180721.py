"""
456. 132 Pattern

Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.
Example 2:
Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:
Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

Credit to NoAnyLove

Just as jade86, we named ai, aj, ak as s1, s2, s3.

Use a stack to keep track of an increasing sequence, if a number is in the range of this increasing sequence (exclusive), then it is a valid s3. When we meet a number smaller than the top of the stack, we need to start with a new increasing sequence, and we use lo and hi to keep track of previous stacks ranges. If we can find a number within the range (lo, hi), it is also a valid s3.

PS: I was trying to use a list to keep track of the ranges of all increasing equences, but got TLE for TestCase 92/95. Then I found we can merge these ranges, and make it easier and faster.

For example, nums = [8, 10, 4, 6, 2, 3, 5], when we traverse to 5, we would have 3 increasing sequence [8, 10], [4, 6], [2, 3], a number falls into any of these ranges would be a valid s3. To make the comparison easy, we merge these 3 ranges to [3, 10], so we only need to check if a number is within [3, 10], and 5 is the s3 we need.


"""

# Result: AC 68ms 72.55%
# Still didn't understand very well, TBC


class Solution:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        lo = float('inf')
        hi = float('-inf')
        for num in nums:
            print('before', stack, lo, hi)
            if len(stack) >= 2 and stack[0] < num < stack[-1]:
                return True
            
            if lo < num < hi:
                return True
            
            if stack and num < stack[-1]:
                if len(stack) >= 2:
                    lo = min(lo, stack[0])
                    hi = max(hi, stack[-1])
                stack = []
                print('stack dumped')
            print('after', stack, lo, hi)
            stack.append(num)
        
        return False


if __name__ == '__main__':
    from time import time
    sol = Solution()
    t = time()
    ans = sol.find132pattern( [8, 10, 4, 6, 2, 3, 5])
    print('ans: %s\n time: %.3fms' % (ans, (time() - t) * 1000))
