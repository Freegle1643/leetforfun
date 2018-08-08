"""
498. Diagonal Traverse

Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output:  [1,2,4,7,5,3,6,8,9]
Explanation:

Note:
The total number of elements of the given matrix will not exceed 10,000.
"""

# Result AC 124ms 93.19%


class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
        	return []

        r = len(matrix)
        c = len(matrix[0])
        n = r * c
        res = []
        res.append(matrix[0][0])
        
        up = True
        i = j = 0

        while n-1 :
        	if up:
        		if not j+1 >= c and not i-1 < 0:
        			j += 1
        			i -= 1
        		elif j+1 >= c:
        			up = False
        			i += 1
        		else:
        			up = False
        			j += 1
        		res.append(matrix[i][j])
        		n -= 1
        		continue
        	if not up:
        		if not j-1 < 0 and not i+1 >= r:
        			j -= 1
        			i += 1
        		elif i+1 >= r:
        			up = True
        			j += 1
        		else:
        			up = True
        			i += 1
        		res.append(matrix[i][j])
        		n -= 1
        		continue

        return res


if __name__ == '__main__':
    from time import time
    sol = Solution()
    t = time()
    ans = sol.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])     
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))           