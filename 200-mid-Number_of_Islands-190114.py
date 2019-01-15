"""
200. Number of Islands
Medium
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""

#DFS
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.DFSMarking(grid, i, j)
                    cnt += 1
        return cnt

    def DFSMarking(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j]='0'
        self.DFSMarking(grid, i+1, j)
        self.DFSMarking(grid, i-1, j)
        self.DFSMarking(grid, i, j+1)
        self.DFSMarking(grid, i, j-1)


# Union Find
from collections import defaultdict

# disjoint-set node
class DsNode:
    def __init__(self):
        self.rank = 0
        self.parent = self

class DisjointSets:
    # DisjointSets Constructors and public methods.
    def __init__(self):
        self._sets = defaultdict(DsNode)

    def find(self, x):
        # path compression
        while x.parent is not x:
            x.parent = x.parent.parent
            x = x.parent
        return x

    def findByLabel(self, label):
        return self.find(self._sets[label])

    def unionByLabel(self, labelA, labelB):
        # union by rank
        a, b = self.find(self._sets[labelA]), self.find(self._sets[labelB])
        if a is not b:
            if a.rank > b.rank:
                b.parent = a
            else:
                a.parent = b
                if a.rank == b.rank:
                    b.rank += 1

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        if rows > 0:
            cols = len(grid[0])
            if cols > 0:
                ds = DisjointSets()
                labels, next_label = [[0]*cols for _ in range(rows)], 1
                for row in range(rows):
                    for col in range(cols):
                        if grid[row][col] == '1':
                            # land, check get north and west
                            north, west = row - 1, col - 1
                            if north >= 0:
                                # use label of north cell for now
                                labels[row][col] = labels[north][col]
                            if west >= 0 and grid[row][west] == '1':
                                if labels[row][col] == 0:
                                    # current cell not labeled, use label of west
                                    labels[row][col] = labels[row][west]
                                elif labels[row][col] != labels[row][west]:
                                    # labels of north and west are different, union the two labels
                                    ds.unionByLabel(labels[row][col], labels[row][west])
                            if labels[row][col] == 0:
                                # current cell not labeled: must be an isolated cell. Use next label
                                labels[row][col] = next_label
                                next_label += 1
                node_set = set()
                for label in range(1, next_label):
                    node_set.add(ds.findByLabel(label))
                return len(node_set)

        return 0
