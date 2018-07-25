"""
319. Bulb Switcher

There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the i-th round, you toggle every i bulb. For the n-th round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

Example:

Input: 3
Output: 1 
Explanation: 
At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off]. 

So you should return 1, because there is only one bulb is on.

Thoughts:

Credit at MrXu_LeetCoder

How many "on" at the end of nth toggle?

--> "on" or "off" at each position in an array of length n?

--> toggle even number times will result in "on", toggle odd number times will result in "off"

--> for position k, the number of toggles is the number of distinct divisors that k has

--> divisors always come in pair, which means even number of divisors, for example, 12 has (1,12),(2,6),(3,4).

--> however, Square Number has odd number of divisors, e.g. 25 has 1,25,5

--> thus, the number of "on", is the number of perfect square number <= n


Thoughts:

credit at StefanPochmann

A bulb ends up on iff it is switched an odd number of times.

Call them bulb 1 to bulb n. Bulb i is switched in round d if and only if d divides i. So bulb i ends up on if and only if it has an odd number of divisors.

Divisors come in pairs, like i=12 has divisors 1 and 12, 2 and 6, and 3 and 4. Except when i is a square, like 36 has divisors 1 and 36, 2 and 18, 3 and 12, 4 and 9, and double divisor 6. So bulb i ends up on if and only if i is a square.

So just count the square numbers.

return int(math.sqrt(n))

i=0
while i*i<=n:
    i+=1
return i-1 

"""


class Solution:
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n))