"""
135. Candy

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.


Thoughts:

Go through via two different direction, combine the result with max value


"""

class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        increase = []
        for i in range(len(ratings)):
            if i == 0:
                increase.append(1)
            elif ratings[i] > ratings[i-1]:
                increase.append(increase[-1]+1)
            else:
                increase.append(1)
        
        ratings = ratings[::-1]
        decrease = []
        for i in range(len(ratings)):
            if i == 0:
                decrease.append(1)
            elif ratings[i] > ratings[i-1]:
                decrease.append(decrease[-1]+1)
            else:
                decrease.append(1)        
        decrease = decrease[::-1]        
                
        res = [max(increase[i],decrease[i]) for i in range(len(ratings))]  

        return sum(res)