"""
95. Unique Binary Search Trees II

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

https://leetcode.com/problems/unique-binary-search-trees-ii/discuss/139169/python-solution-with-dp
"""

# Result AC 120ms  4.31%
# TBC


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def helper(m, n):
            if m == n:
                return [TreeNode(m)]
            if m > n:
                return [None]
            ans = []
            for i in range(m, n+1):
                left = helper(m, i-1)
                right = helper(i+1, n)
                for j in range(len(left)):
                    for k in range(len(right)):
                        root = TreeNode(i)
                        root.left = left[j]
                        root.right = right[k]
                        ans.append(root)
            return ans
        
        if n == 0:
            return []
        return helper(1, n)