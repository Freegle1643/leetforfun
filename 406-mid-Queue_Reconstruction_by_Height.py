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