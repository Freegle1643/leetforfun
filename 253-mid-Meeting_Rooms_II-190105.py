"""
253. Meeting Rooms II

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
"""


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals: return 0

        intervals = sorted(intervals, key = lambda x: x.start)
        heap = []
        heapq.heapify(heap)

        for interval in intervals:
        	if heap and heap[0] <= interval.start: heapq.heapreplace(heap, interval.end)
        	else: heapq.heappush(heap, interval.end)
        return len(heap)




        # if not intervals:
        # 	return 0
        # starts = sorted(interval.start for interval in intervals)
        # ends = sorted(interval.end for interval in intervals)
        # rooms = 0
        # Ptr = 0
        # for start in starts:
        # 	if start < ends[Ptr]:
        # 		rooms += 1
        # 	else:
        # 		Ptr += 1
        # return rooms
