"""
54. Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Ex. 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Ex. 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Thoughts:

1. Four types of operation, right, down, left, up. 
2. Four types of spiral. draw 1,2,3,4 rows then you will know what I mean.


"""

# Result: AC 32ms 100 %

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix or not matrix[0]:
            return res
        while matrix:
            # right, first entire row
            res += matrix.pop(0)
            #down, includes the last element of last row
            if matrix:
                for row in matrix:
                    if row:
                        res.append(row.pop())
                    else:
                        return res
            else:
                return res
            #left, start from second to last element of last row
            if matrix[-1]:
                res += matrix.pop()[::-1]
            else:
                return res
            #up
            if matrix:
                for row in matrix[::-1]:
                    if row:
                        res.append(row.pop(0))
                    else:
                        return res
            else:
                return res
        return res