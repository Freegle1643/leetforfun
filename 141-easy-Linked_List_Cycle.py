"""
141. Linked List Cycle

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

Note:
1. If two runner running at different constant speed on a circle track, they will eventually meet each other.
	See more on https://leetcode.com/problems/linked-list-cycle/solution/
2. Line 31 'if slow is fast:' DO NOT USE '=='. Since if two different LinkNode have the same value, such condition would lead to a wrong decision.
	More on https://dbader.org/blog/difference-between-is-and-equals-in-python
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        # Two runner at different speed
        # Slow at 1, Fast at 2
        slow = fast = head

        while fast and fast.next :
        	slow = slow.next
        	fast = fast.next.next
        	if slow is fast:
        		return True
        return False
