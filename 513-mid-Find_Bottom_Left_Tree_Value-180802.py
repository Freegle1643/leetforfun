"""
513. Find Bottom Left Tree Value

Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2: 
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.
"""

# Result AC 56ms 76.96%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x 
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
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
                
        return level_info[sorted(level_info)[-1]][0]