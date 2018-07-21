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
"""

# Result: AC 76ms 55.86%


class Solution:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) < 3:
            return False
        min_nums = [nums[0]]
        min_val = nums[0]
        for i in range(1, len(nums)):
            if min_val < nums[i]:
                min_nums.append(min_val)
            else:
                min_nums.append(nums[i])
                min_val = nums[i]
        stack = [nums[-1]]
        print(min_nums)
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > min_nums[i]:
                while stack and stack[-1] <= min_nums[i]:
                    stack.pop()
                if stack and stack[-1] < nums[i]:
                    return True
                stack.append(nums[i])
        return False


if __name__ == '__main__':
    from time import time
    sol = Solution()
    t = time()
    ans = sol.find132pattern([-1, 3, 2, 0])
    print('ans: %s\n time: %.3fms' % (ans, (time() - t) * 1000))
