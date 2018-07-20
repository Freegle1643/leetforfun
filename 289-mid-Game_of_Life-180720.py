"""
289. Game of Life

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]

Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?


Thoughts:
1. A) 1 -> <2 -> 0 B) 1 -> 2,3 -> 1 C) 1 -> >3 -> 0 D) 0 -> 3 -> 1
2. If neighbors are B or D, add 10 to each value. Other live remains 1, when divided by 10, they will die and others will live.

"""


# Result AC 48 ms 3.98%
# That's embarrassing


class Solution(object):
    def gameOfLife(self, board):
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                neighbors = self.getNeighbors(board, i, j)
                # Currently Dead
                if board[i][j] == 0:
                    if neighbors == 3:
                        board[i][j] += 10  # Dead -> Live
                # Currently Live
                elif neighbors == 2 or neighbors == 3:
                	board[i][j] += 10  # Live -> Live

                # Other Live cells will turns to 0 when / 10
        
        # In-place bitwise operation
        for i in range(m):
            for j in range(n):
                board[i][j] //= 10
        return
    
    def getNeighbors(self, board, row, col):
        m, n = len(board), len(board[0])
        cnt = 0 
        for i in [row-1, row, row+1]:
            for j in [col-1, col, col+1]:
                if i == row and j == col or i < 0 or j < 0 or i >= m or j >= n:
                    continue
                if board[i][j] % 10 == 1:
                    cnt += 1
        return cnt

if __name__ == '__main__':
    from time import time
    sol = Solution()
    t = time()
    board = [[0,1,0], [0,0,1], [1,1,1], [0,0,0]]
    ans = sol.gameOfLife(board)     
    print('ans: %s\ntime: %.3fms' % (board, ((time() - t)) * 1000))          