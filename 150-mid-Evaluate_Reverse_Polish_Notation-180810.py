"""
150. Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

Same idea using lambda

def evalRPN(self, tokens):
    op = {
    '+': lambda x: lambda y: int(float(x)+float(y)),
    '-': lambda x: lambda y: int(float(x)-float(y)),
    '*': lambda x: lambda y: int(float(x)*float(y)),
    '/': lambda x: lambda y: int(float(x)/float(y))
    }
    s = []
    for i in tokens:
        if i in ['+','-','*','/']:
            [n1, n2] = s[-2:]
            s[-2:] = [op[i](n1)(n2)]
        else:
            s.append(int(i))
    return s[0]

"""

# Result 48ms 51.30%


class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t not in ["+", "-", "*", "/"]:
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(int(float(l)+float(r)))
                elif t == "-":
                    stack.append(int(float(l)-float(r)))
                elif t == "*":
                    stack.append(int(float(l)*float(r)))
                else:
                	stack.append(int(float(l)/float(r)))
                    
        return stack.pop()