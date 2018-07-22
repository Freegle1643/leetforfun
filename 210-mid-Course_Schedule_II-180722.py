"""
210. Course Schedule II

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.

"""

# Result: AC 80ms 22.55%

from collections import defaultdict, deque


class Solution:
	def findOrder(self, numCourses, prerequisites):
		# has_req stores pre-req of courses, if any
	    has_req = {i: set() for i in range(numCourses)}
	    # is_req stores what courses has them as pre-req
	    is_req = defaultdict(set)
	    for i, j in prerequisites:
	        has_req[i].add(j)
	        is_req[j].add(i)
	    # queue stores the courses which have no prerequisites
	    queue = deque([i for i in has_req if not has_req[i]])
	    count, res = 0, []
	    while queue:
	        node = queue.popleft()
	        res.append(node)
	        count += 1
	        for i in is_req[node]:
	        	# clear pre-req since course(i.e. node) has been taken
	            has_req[i].remove(node)
	            if not has_req[i]:
	            	# when a course has no req, add it to queue
	                queue.append(i)
	    return res if count == numCourses else []


if __name__ == '__main__':
    from time import time
    sol = Solution()
    t = time()
    ans = sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
    print('ans: %s\ntime: %.3fms' % (ans, (time() - t) * 1000)) 	   