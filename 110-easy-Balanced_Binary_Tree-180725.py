"""
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.


"""

# Result 72ms 45.83%


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def parse(self, node, depth):
        if node == None:
            return depth, True
        l_height, l_balanced = self.parse(node.left, depth+1)
        r_height, r_balanced = self.parse(node.right, depth+1)
        diff = abs(l_height - r_height)
        if diff > 1:
            return max(l_height, r_height), False
        return max(l_height, r_height), l_balanced and r_balanced
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        height, balanced = self.parse(root, 0)
        return balanced
     