"""
134. Gas Station

There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:

If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.

Ex.1

Input: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Ex.2

Input: 
gas  = [2,3,4]
cost = [3,4,3]

Output: -1

Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.

Thoughts:

1. Construct a gap list, each element is gas[i] - cost[i]. If the sum of every element is less negative, there's no solution.
2. If there are elements in gap list that are negative, those gas station could not be start point.
3. Go through those non-negative gas station, emulate the whole process. Print the first gas station i that fits.(According to the question, only one solution is match. So first is the only one.)
4. *Pay attention to foot index of gap list, since we go through the list in CIRCULAR manner.

Improved Thoughts:

Credit at ringabel

So how do you pick where to start? 
First, each station will either give you a gas surplus (if it requires less gas to go to the next station than it has at the station), or a gas deficit (if it's the other way around). 
So your total gas supply either rises or shrinks as you pass through each station (draw a curve yourself. It will look like a movement of a stock). 
The most difficult part of the trip is when your gas supply continues to shrink. Now assume your gas can go negative, and you have to start from station 0, the most difficult time is when your gas supply is the lowest (most negative). 
The trick is to pick the station right after the most difficult time. Then your gas always stays positive!


"""

# Result: AC 44ms 26.87% 
# Even using this trick, 26.87% is still so low
# The leading part of the solution also implement such thoughts, but with a faster code

class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        tank = 0
        min_gas, min_gas_loc = 0, None
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < min_gas:
                min_gas = tank
                min_gas_loc = i
        return 0 if min_gas_loc is None else (min_gas_loc + 1) % len(gas)
