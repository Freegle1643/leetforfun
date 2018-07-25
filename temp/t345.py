class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        v_ori = []
        for i in s:
        	if i in vowels:
        		v_ori.append(i)

        k = 0

        l = len(s)
        print(v_ori,'l:',l)
        for j in range(l - 1, -1, -1):
        	print(s)
        	print('j:', j, 's[', j, ']=', s[j])
        	if s[j] in vowels:
        		print('k:',k)
        		print('s[:j-1]=s[:',j-1,']',s[:j - 1], v_ori[k], 's[j + 1:]=s[',j+1,':]',s[j + 1:])
        		s = s[:j] + v_ori[k] + s[j + 1:]
        		k += 1

        return s


if __name__ == '__main__':
	from time import time
	sol = Solution()
	t = time()
	ans = sol.reverseVowels('leotcede')
	print('ans: %s\ntime: %.3fms' % (ans, (time() - t) * 1000)) 