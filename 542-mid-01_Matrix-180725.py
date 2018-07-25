"""
542. 01 Matrix

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
Example 1: 
Input:

0 0 0
0 1 0
0 0 0
Output:
0 0 0
0 1 0
0 0 0
Example 2: 
Input:

0 0 0
0 1 0
1 1 1
Output:
0 0 0
0 1 0
1 2 1
Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.

"""

# Result AC 400 ms 96.94%
# TBC Not familiar with DP


class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        dic = {}
        if not matrix or not matrix[0]:
            return matrix
        h, w = len(matrix),len(matrix[0])
        mask = [[10000] * w for i in range (h)]
        for i in range (h):
            for j in range (w):
                if matrix[i][j] != 0:
                    mask[i][j] = min(mask[i][j],mask[i - 1][j] + 1,mask[i][j - 1] + 1)
                else:
                    mask[i][j] = 0
        for i in range (h - 1, -1, -1):
            for j in range (w - 1, -1, -1):
                if matrix[i][j] != 0:
                    if i < h - 1:
                        mask[i][j] = min(mask[i][j],mask[i + 1][j] + 1)
                    if j < w - 1:
                        mask[i][j] = min(mask[i][j],mask[i][j + 1] + 1)
        return mask