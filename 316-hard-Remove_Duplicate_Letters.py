# 143 / 286 Passed, Others are wrong TBC

from collections import OrderedDict

class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmp = "".join(OrderedDict.fromkeys(s))
        return (''.join(sorted(tmp)))