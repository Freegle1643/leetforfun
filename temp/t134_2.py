"""
Another implementation of improved thoughts. AC but in relatively the same range.

"""

class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        n, station, rest_gas = len(gas), 0, 0
        for i in range(n):
            if gas[i] + rest_gas < cost[i]:
                station, rest_gas = i + 1, 0
            else:
                rest_gas += gas[i] - cost[i]
        return station