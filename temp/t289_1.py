"""
https://leetcode.com/problems/game-of-life/discuss/140520/Python3-in-place-compact-with-list-comprehensions
"""



class Solution:
    ALIVE = 1
    DEAD = 0
    BORN = 2
    DYING = -1

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i, j in [(i,j) for i in range(len(board)) for j in range(len(board[i]))]:
            lives = self.live_neighbors(board, i, j)
            if board[i][j] == self.DEAD and lives == 3:
                board[i][j] = self.BORN
            elif board[i][j] == self.ALIVE and lives not in [2,3]:
                board[i][j] = self.DYING

        for i, j in [(i,j) for i in range(len(board)) for j in range(len(board[i]))]:
            if board[i][j] == self.BORN:
                board[i][j] = self.ALIVE
            if board[i][j] == self.DYING:
                board[i][j] = self.DEAD

    def live_neighbors(self, board, x, y):
        count = 0
        for (r, c) in [(x + i, y + j) for i in [-1, 0, 1] for j in [-1, 0, 1] if not i == j == 0]:
            if not (r < 0 or c < 0 or r >= len(board) or c >= len(board[0])) and board[r][c] in (self.ALIVE, self.DYING):
                count += 1
        return count