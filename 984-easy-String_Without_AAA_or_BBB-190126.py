"""
984. String Without AAA or BBB
Difficulty: Easy
Given two integers A and B, return any string S such that:

S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
The substring 'aaa' does not occur in S;
The substring 'bbb' does not occur in S.


Example 1:

Input: A = 1, B = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.
Example 2:

Input: A = 4, B = 1
Output: "aabaa"


Note:

0 <= A <= 100
0 <= B <= 100
It is guaranteed such an S exists for the given A and B.
"""

class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        res = ''
        while A or B:
            if len(res) >= 2 and res[-1]==res[-2]:
                append_A = res[-1] == 'b'
            else:
                append_A = A >= B

            if append_A:
                A -= 1
                res += 'a'
            else:
                B -= 1
                res += 'b'

        return res
