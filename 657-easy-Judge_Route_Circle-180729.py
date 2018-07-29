"""
657. Judge Route Circle

Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
"""

# Result AC 80 ms 18.96%
# Or simply use counter in Python return (moves.count('U') == moves.count('D')) and (moves.count('R') == moves.count('L'))


class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        mov = {'L': 0, 'R':0, 'U': 0, 'D': 0}
        for move in moves:
        	if move == 'L':
        		if mov['R']:
        			mov['R'] -= 1
        		else:
        			mov['L'] += 1
        	elif move == 'R':
        		if mov['L']:
        			mov['L'] -= 1
        		else:
        			mov['R'] += 1
        	elif move == 'U':
        		if mov['D']:
        			mov['D'] -= 1
        		else:
        			mov['U'] += 1
        	elif move == 'D':
        		if mov['U']:
        			mov['U'] -= 1
        		else:
        			mov['D'] += 1

       	s = 0
        for m in mov:
        	s += mov[m]
        return True if s == 0 else False