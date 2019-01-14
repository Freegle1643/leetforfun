"""
31. Next Permutation
Medium
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

algorithm attached below
https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
"""

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # identify the longest non-increasing sub-sequence
        right = len(nums)-1
        while(nums[right] <= nums[right-1] and right-1 >= 0):
            right -= 1
        if right == 0:
            return self.reverse(nums, 0, len(nums)-1)

        pivot = right-1
        for i in range(len(nums)-1, pivot, -1):
            if nums[i] > nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                successor = i
                break

        self.reverse(nums, pivot+1, len(nums)-1)

    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
