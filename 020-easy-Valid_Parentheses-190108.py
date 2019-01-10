"""
20. Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        # Using a dictionary
        mapping = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in mapping:
                top = stack.pop() if stack else "#"
                if mapping[c] != top:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

        """
        Foolish thoughs
        """
        # cnt1, cnt2, cnt3 = 0, 0, 0
        # for c in s:
        #     if c == "(":
        #         cnt1 += 1
        #     elif c == "{":
        #         cnt2 += 1
        #     elif c == "[":
        #         cnt3 += 1
        #     elif c == ")":
        #         cnt1 -= 1
        #     elif c == "}":
        #         cnt2 -= 1
        #     elif c == "]":
        #         cnt3 -= 1
        # return True if (cnt1 == 0 and cnt2 == 0 and cnt3 == 0) else False
