"""
143. Reorder List


Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""

# Result AC 96ms 99.69%
# TBC


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None:
            return
        p = head
        q = head
        # slow pointer p and quick pointer q
        while q is not None and q.next is not None:
            q = q.next.next
            p = p.next
        # find middle
        mid = p.next
        p.next = None
        begin = head
        end = mid
        pre = None
        # reverse link
        while end is not None:
            temp = end.next
            end.next = pre
            pre = end
            end = temp
        # merge link
        while pre is not None and begin is not None:
             a = pre.next
             b = begin.next
             begin.next = pre
             pre.next = b
             begin = b
             pre = a
        return