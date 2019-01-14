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

"""
DFS on code, looks simliar to backtracking
https://leetcode.com/problems/generate-parentheses/solution/
Backtracking is an algorithmic-technique for solving problems recursively by trying to
build a solution incrementally, one piece at a time, removing those solutions that fail to
satisfy the constraints of the problem at any point of time (by time, here, is referred to
the time elapsed till reaching any level of the search tree).
https://www.geeksforgeeks.org/backtracking-algorithms/
"""

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return []
        left, right, ans = 0, 0, []
        def backtracking(left, right, ans, str):
            if left + right == 2 * n:
                ans.append(str)
                return
            if left < n:
                backtracking(left+1, right, ans, str+"(")
            if right < left:
                backtracking(left, right+1, ans, str+")")

        backtracking(left, right, ans, "")
        return ans



"""
DP Solution
https://leetcode.com/problems/generate-parentheses/discuss/10369/Clean-Python-DP-Solution

"""
class Solution(object):
    def generateParenthesis(self, n):
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]
