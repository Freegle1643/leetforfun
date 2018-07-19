"""
93. Restore IP Addresses

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]

Thoughts:

Credit @ garudy

Define a validation function and then determine whether four part of the string is valid individually.

"""

# Results: AC 44ms 72.92%

class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isPartValid(s):
            size = len(s)
            if size == 0 or (size > 1 and s[0] == "0") or size > 3:
                return False
            
            val = int(s)
            if val >= 0 and val < 256:
                #print(val)
                return True
            
        result = []
        size = len(s)
        
        if size < 4:
            return result
        
        
        for i in range(4):
                subi = s[:i]
                if isPartValid(subi):
                    for j in range(i, i+4):
                        if j < size:
                            subj = s[i:j]
                            if isPartValid(subj):
                                for k in range(j, j+4):
                                    if k < size:
                                        subk = s[j:k]
                                        subl = s[k:]
                                        if isPartValid(subk) and isPartValid(s[k:]):
                                            result.append(subi + "." + subj + "." + subk + "." + subl)
                                        
                                        
        return result        


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.restoreIpAddresses('111111')     
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))        