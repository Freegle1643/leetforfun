"""
904. Fruit Into Baskets
Medium
In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?



Example 1:

Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].
Example 2:

Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].
Example 3:

Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].
Example 4:

Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.


Note:

1 <= tree.length <= 40000
0 <= tree[i] < tree.length

Intuitive thoughs, longest consecutive sequence that contains only two kind numbers
LeetCode says it's two pointers
...
Well, indeed, it's a two pointers problem. last and last_s, thoese are two pointers.
"""

class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        if not tree:
            return 0
        tree_kind = [] # list that stores current two kinds of trees
        cnt = 0
        maximum = 1
        last = 0    # treekind last seen
        last_s = 0  # last seen treekind start index

        for i in range(len(tree)):
            if len(tree_kind) < 2:
                if not tree[i] in tree_kind:
                    tree_kind.append(tree[i])
                    last_s = i
            else:   # already two kinds of trees
                if tree[i] in tree_kind:    # still those two kinds
                    last_s = i if tree[last_s] != tree[i] else last_s
                else:   # new tree kind appears
                    maximum = max(cnt, maximum)
                    tree_kind[1-tree_kind.index(last)] = tree[i]    #update tree kinds
                    cnt = i - last_s
                    last_s = i
            last = tree[i]
            cnt += 1

        return max(maximum, cnt)
