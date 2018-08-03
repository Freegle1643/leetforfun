"""
204. Count Primes

Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.


def countPrimes(self, n):
    if n < 3:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
    return sum(primes)


"""

# Resutl AC 488ms 60.45%


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        n -= 1
       	if n < 2:
       		return 0

       	marker = [1] * (n+1)
       	marker[0] = marker[1] = 0

       	for i in range(2, int(n ** 0.5) + 1):
       		if marker[i]:
       			for j in range(i + i, n + 1, i):
       				marker[j] = 0

       	return sum(marker)


if __name__ == '__main__':
	sol = Solution()
	from time import time
	t = time()
	ans = sol.countPrimes(10)
	print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))  