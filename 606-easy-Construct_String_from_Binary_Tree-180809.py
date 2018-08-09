"""
606. Construct String from Binary Tree

You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())", 
but you need to omit all the unnecessary empty parenthesis pairs. 
And it will be "1(2(4))(3)".
Example 2:
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example, 
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.

"""

# Result AC 68ms 51.67%
# TBC


class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def preorder(t, s):
            s.append('(')
            if t is not None:
                s.append(str(t.val))
                if not (t.left is None and t.right is None):
                    preorder(t.left, s)         #when t.left is None, we need '()', so no need to check
                    if t.right is not None:     #check t.right, because we omit it when it is None
                        preorder(t.right, s)
            s.append(')')
        ans = []
        preorder(t, ans)
        return "".join(ans)[1:-1]       #the root node does not need '()' around it, so we omit the first and the last char