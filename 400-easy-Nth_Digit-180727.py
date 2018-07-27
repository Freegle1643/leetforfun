"""
400. Nth Digit

Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.

"""


# Result AC 20ms 100%


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = 9
        d = 2
        padding = 0

        if n >= 1 and n <= 9:
        	return n
        
        while True:
        	left += 9 * (10 ** (d-2)) * (d-1)
        	right += 9 * (10 ** (d-1)) * (d)
        	print('[',left,',',right,']')
        	if n >= left and n <= right:
        		padding = n - (left - 1)
        		print('padding', padding)
        		break
        	d += 1

        num, cnt = divmod(padding, d)
        print(num, cnt, d)
        if cnt == 0:
        	print(str((10 ** (d-1)) -1 + num))
        	return int(str((10 ** (d-1)) -1 + num)[-1])
        else:
        	print(str((10 ** (d-1)) + num))
        	return int(str((10 ** (d-1)) + num)[cnt-1])



if __name__ == '__main__':
	from time import time
	sol = Solution()
	t = time()
	ans = sol.findNthDigit(11)
	print('ans: %s\ntime: %.3fms' % (ans, (time() - t) * 1000)) 