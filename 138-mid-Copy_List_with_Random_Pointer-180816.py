"""
138. Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

Notes:
1. Ituitive thoughts will lead to O(2n) solution
"""

# Result AC 72ms 85.01%


# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        tree = dict()
        p = q = head
        while p:
        	tree[p] = RandomListNode(p.label)
        	p = p.next
        while q:
        	tree[q].next = tree.get(q.next)
        	tree[q].random = tree.get(q.random)
        	q = q.next
        return tree.get(head)