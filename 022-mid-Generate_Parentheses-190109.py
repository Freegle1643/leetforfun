"""
22. Generate Parentheses
Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

https://leetcode.com/problems/generate-parentheses/discuss/10110/Simple-Python-DFS-solution-with-explanation

"""


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return []
        left, right, ans = n, n, []
        self.dfs(left, right, ans, "")
        return ans

    def dfs(self, left, right, ans, string):
        # not enough left open pair
        if right < left:
            return
        # generated valid answer
        if not left and not right:
            ans.append(string)
            return
        # if we can add more left pair
        if left:
            self.dfs(left-1, right, ans, string + "(")
        # if we can add more right pair and there are fewer or equal left pair we have
        if right:
            self.dfs(left, right-1, ans, string + ")")
