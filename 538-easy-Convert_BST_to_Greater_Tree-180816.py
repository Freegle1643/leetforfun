"""
538. Convert BST to Greater Tree

Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
"""

# Result AC 92ms 89.59%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.cur_sum = 0
        self.convertHelper(root)
        return root

    def convertHelper(self, root):
        if not root:
            return
        self.convertHelper(root.right)
        root.val += self.cur_sum
        self.cur_sum = root.val
        self.convertHelper(root.left)