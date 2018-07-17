"""
142. Linked List Cycle II

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?

Note:
1. Use exactly what 141 uses to reduce space consumption
2. Add things after identify there's a circle
3. Math calculation like https://leetcode.com/problems/linked-list-cycle-ii/discuss/150666/c++-4ms-beats-100
    Let us give the distance a variable name, x, y and z.
    [head] ---x---> [Cycle_Start] ---y---> [MeetPoint](fast/slow runner) ---z---> [Cycle_Start]
    At this moment, fast and slow runner are both at [MeetPoint].
    The problem is equal to "How many steps should slow runner run to [Cycle_Start]?".
    In other words, "How many steps is z distance?"
    The distance run by slow runner = x + y
    The distance run by fast runner = x + y + z + y
    Since fast runner is two times faster than slow runner.
    fast = 2 * ( slow )
    x + y + z + y = 2 * ( x + y )
    x + 2y + z = 2x + 2y
    z = x
    It means slow runner should run z steps to [Cycle_Start] point from [MeetPoint].
    And z distance is the same as x distance.
4. What we add is that we put slow and fast to [MeetPoint] and [Head], let them run at SAME pace. When they meet, fast covered x and slow covered z, which is equal to x. The LinkNode would be the entry of circle.
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        # Two runner at different speed
        # Slow at 1, Fast at 2
        slow = fast = head

        while fast and fast.next :
        	slow = slow.next
        	fast = fast.next.next
        	if slow is fast: # Circle found
                    fast = head
                    while fast is not slow:
                        slow = slow.next
                        fast = fast.next
                    return fast
        return None
   