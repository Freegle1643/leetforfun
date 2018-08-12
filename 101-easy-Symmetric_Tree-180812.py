"""
101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""

# Result AC 44ms 84.39%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
        	return True
        else:
        	return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
    	if left is None and right is None:
    		return True
    	elif left is None or right is None:
    		return False

    	elif left.val == right.val:
    		outPair = self.isMirror(left.left, right.right)
    		inPair = self.isMirror(left.right, right.left)
    		return outPair and inPair

    	else:
    		return False