"""
461. Hamming Distance

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""

"""
# Result AC 24ms 38.18%


class Solution(object):
    def hammingDistance(self, x, y):
        return bin(x^y).count('1')

"""

# Result AC 20ms 100%


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        binx = bin(x)[2:]
        biny = bin(y)[2:]
        while(len(binx) > len(biny)):
            biny = "0"+biny
        while(len(biny) > len(binx)):
            binx = "0"+binx
        counter = 0
        for i in range(len(binx)):
            if binx[i] !=biny[i]:
                counter+=1
        return counter