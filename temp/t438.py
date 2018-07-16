from collections import defaultdict

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        if len(s)<len(p) :
            return []

        # We use two dictionary dp/dt and ds, dp is initialized with all values equal to the amount of a alphabet.
        # If we find a match charactor, the value of corresponding key-value pair in dp would decrease by 1.
        # If after len(p) steps, all the values in dp are 0, put corresponding index of s in result.

        dp = defaultdict(int)

        # for i in range(len(p)) :
        #     dp[p[i]] = int(0)

        for i in range(len(p)) :
            dp[p[i]] = int(dp[p[i]]) + 1

        results = []

        for j in range(0, len(s)-len(p)+1):
            # print(j)
            if s[j] in dp:
                dt = dp.copy()
                # print(dp)
                dt[s[j]] -= 1 # cross that charactor in this run

                t = j + 1

                for k in range(len(p) - 1):
                    if s[t] in dt and dt[s[t]] != 0: # another charactor match and it has not been crossed
                        # print('next')
                        dt[s[t]] -= 1
                        t += 1

                # print(t)

                if t - j == len(p): # successfully cross len(p) charactors
                    # print('add')
                    results.append(j)

            # else:
            #   break

            # print(j)

        return results


                        
if __name__ == '__main__':
    print(Solution().findAnagrams('baa', 'aa'))
