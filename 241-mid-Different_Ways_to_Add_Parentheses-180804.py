"""
241. Different Ways to Add Parentheses

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
"""


class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """

        if input.isdigit():
        	return [int(input)]

        res = []
        for i in range(len(input)):
        	if input[i] in "+*-":
        		res1 = self.diffWaysToCompute(input[:i])
        		res2 = self.diffWaysToCompute(input[i+1:])
        		for j in res1:
        			for k in res2:
        				res.append(self.helper(int(j), int(k), input[i]))

        return res

    def helper(self, left, right, op):
    	if op == '+':
    		return left + right
    	if op == '-':
    		return left - right
    	if op == '*':
    		return left * right


if __name__ == '__main__':
    from time import time
    sol = Solution()
    t = time()
    ans = sol.diffWaysToCompute("2-1-1")     
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))  