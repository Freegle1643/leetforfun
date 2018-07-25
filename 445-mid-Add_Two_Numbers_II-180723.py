"""
445. Add Two Numbers II

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""

from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        v1 = 0
        d1 = l1
        v2 = 0
        d2 = l2
        vr = 0
        while d1.next:
        	v1 = v1 * 10 + d1.val
        	d1 = d1.next
        while d2.next:
        	v2 = v2 * 10 + d2.val
        	d2 = d2.next
        vr = v1 + v2
        str_vr = deque(str(vr))
        res = ListNode(str_vr[0])
        str_vr.popleft()
        worker = res        
        for i in range(len(str_vr)):
        	worker.next = ListNode(str_vr.popleft())
        	worker = worker.next
        return res
