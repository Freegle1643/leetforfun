"""
102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]

"""

from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        level_info = defaultdict(list)
        
        level = 0
        queue = [(root, level)]
        
        while queue:
            node, level = queue.pop(0)
            level_info[level].append(node.val)
            level += 1
            if node.left:
                queue.append((node.left, level))
            if node.right:
                queue.append((node.right, level))
                
        return list(level_info.values())