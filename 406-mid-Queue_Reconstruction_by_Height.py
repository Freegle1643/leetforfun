"""
406. Queue Reconstruction by Height

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

*The number of people is less than 1,100.


Ex.1 

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

Note:
1. The so called reconstruct is to output any order that makes sense.
2. This discussion explains thing perfectly. It illustrate divide and conqure. https://leetcode.com/problems/queue-reconstruction-by-height/discuss/89345/Easy-concept-with-PythonC++Java-Solution


"""


# Result: AC
# Deeper understanding required | TBC

class Solution(object):
    def reconstructQueue(self, people):
        if not people: return []

        # get people's info
        # key=h, value=k, index in original array
        pdict, height, results = {}, [], []
        
        for i in xrange(len(people)):
            p = people[i]
            if p[0] in pdict:
                pdict[p[0]] += (p[1], i),
            else:
                pdict[p[0]] = [(p[1], i)]
                height += p[0],

        height.sort()      # here are different heights we have

        # sort from the tallest group
        for h in height[::-1]:
            pdict[h].sort()
            for p in pdict[h]:
                results.insert(p[0], people[p[1]])

        return results